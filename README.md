# crbug394235958
Chromium iOS Bug Report #394235958 test case: iOS Wallet Order packages (application/vnd.apple.finance.order ZIPs) aren't handled properly

# Testing
- Start the server with `python server.py`.
  - Optionally use `ngrok http http://localhost:8080` to make the test available on your mobile phone
- Open the site on your mobile Chrome Browser on iOS
- Click the pkpass/pkpasses links and see the overlay displaying the Wallet Pass information.
- Click the test.order link and see that Chrome wants to download the test.order file, instead of showing the Order in an overlay.

Positive Test Case:
- Open the test site on mobile Safari
- Click the test.order link and see Safari showing an overlay displaying the test order.
