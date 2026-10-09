// പാസ്‌വേഡ് കാണാനും മറയ്ക്കാനുമുള്ള ഫങ്ഷൻ
function togglePass() {
    const passInput = document.getElementById('password');
    const toggleBtn = document.querySelector('.toggle-password');
    
    if (passInput) {
        if (passInput.type === 'password') {
            passInput.type = 'text';
            toggleBtn.textContent = 'Hide';
        } else {
            passInput.type = 'password';
            toggleBtn.textContent = 'Show';
        }
    }
}

// HTML-ലെ onclick-ന് പകരം JS വഴി ക്ലിക്ക് ലിസണർ കൊടുക്കുന്നു
document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.querySelector('.toggle-password');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', togglePass);
    }
});

// ലോഗിൻ ഫോം ഹാൻഡ്‌ലിംഗ്
document.getElementById('loginForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const user = document.getElementById('username').value;
    const pass = document.getElementById('password').value;

    if (user && pass) {
        console.log("Authenticating:", user);
        
        // ലോഗിൻ വിജയിച്ചാൽ 2FA സ്ക്രീൻ കാണിക്കുന്നു
        document.getElementById('loginCard')?.classList.add('hidden');
        document.getElementById('otpCard')?.classList.remove('hidden');
    }
});

// OTP വേരിഫിക്കേഷൻ
document.getElementById('otpForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const otp = document.getElementById('otpInput').value;
    
    if (otp.length === 6) {
        alert("2FA Verification Successful! Redirecting to Dashboard...");
    } else {
        alert("ദയവായി 6-ഡിജിറ്റ് OTP കൃത്യമായി നൽകുക.");
    }
});
