from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, View
from django.http import JsonResponse
from .forms import UserRegistrationForm, UserAddressForm
from .digital_signature import sign_data, verify_signature
from .encryption import encrypt_data, decrypt_data
from .hash_function import calculate_hash
from .key_management import generate_symmetric_key
from Cryptodome.PublicKey import RSA

User = get_user_model()

class UserRegistrationView(TemplateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/user_registration.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('transactions:transaction_report'))
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        registration_form = UserRegistrationForm(self.request.POST)
        address_form = UserAddressForm(self.request.POST)

        if registration_form.is_valid() and address_form.is_valid():
            user = registration_form.save()
            address = address_form.save(commit=False)
            address.user = user
            address.save()

            login(self.request, user)
            messages.success(
                self.request,
                f'Thank You For Creating A Bank Account. Your Account Number is {user.account.account_no}.'
            )
            return HttpResponseRedirect(reverse_lazy('transactions:deposit_money'))

        return self.render_to_response(
            self.get_context_data(
                registration_form=registration_form,
                address_form=address_form
            )
        )

    def get_context_data(self, **kwargs):
        if 'registration_form' not in kwargs:
            kwargs['registration_form'] = UserRegistrationForm()
        if 'address_form' not in kwargs:
            kwargs['address_form'] = UserAddressForm()

        return super().get_context_data(**kwargs)

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    redirect_authenticated_user = True

class LogoutView(RedirectView):
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)

# New views for cryptographic operations

class SignMessageView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST['data']
        private_key = RSA.import_key(bytes.fromhex(request.user.encrypted_private_key))
        signature = sign_data(data, private_key)
        return JsonResponse({'signature': signature.hex()})

class VerifyMessageView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST['data']
        signature = bytes.fromhex(request.POST['signature'])
        public_key = RSA.import_key(request.user.public_key)
        is_valid = verify_signature(data, signature, public_key)
        return JsonResponse({'is_valid': is_valid})

class EncryptMessageView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST['data']
        key = generate_symmetric_key()
        ct_bytes, iv = encrypt_data(data, key)
        return JsonResponse({'ciphertext': ct_bytes.hex(), 'iv': iv.hex(), 'key': key.hex()})

class DecryptMessageView(View):
    def post(self, request, *args, **kwargs):
        ct_bytes = bytes.fromhex(request.POST['ciphertext'])
        iv = bytes.fromhex(request.POST['iv'])
        key = bytes.fromhex(request.POST['key'])
        plaintext = decrypt_data(ct_bytes, iv, key)
        return JsonResponse({'plaintext': plaintext})

class HashMessageView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST['data']
        hash_value = calculate_hash(data)
        return JsonResponse({'hash': hash_value})

