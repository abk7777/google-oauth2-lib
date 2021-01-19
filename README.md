[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]

# google-oauth2-lib

Examples of Python OAuth 2.0 flow for Google Workspace API.

-- Project Status: [Complete]

## Getting Started

### Prerequisites
1. Follow the steps to create OAuth 2.0 authorization credentials for Google API for Mobile & Desktop Apps:
   - [Enable the API](https://developers.google.com/identity/protocols/oauth2/native-app#enable-apis)
   - [Create authorization credentials](https://developers.google.com/identity/protocols/oauth2/native-app#creatingcred)
2. Download the OAuth 2.0 `client_secret.json` file (available in Google Cloud Platform under APIs & Services --> Credentials) and store in project root.

### Setup
(*MacOS/Linux*)
1. Clone the repo:
   ```
   git clone <repo>
   cd <repo>
   ```
2. Create a Python virtual environment:
   ```
   python3 -m venv .venv/
   source .venv/bin/activate
   ```
3. Install packages in the virtual environment:
   ```
   pip install -r requirements.txt
   ```

### Run App
Running this will open a browser window asking you to allow access to your Google Sheets account:
```
python3 example.py
```
The OAuth flow will create a `token.pickle` file containing the valid credentials for the user.

## Reference
- [Google Sheets API v4 Documentation](https://developers.google.com/sheets/api/guides/concepts)
- [Google Sheets API PyDoc documentation](https://developers.google.com/resources/api-libraries/documentation/sheets/v4/python/latest/index.html)

## Contributors

- **Primary (Contact) : [Gregory Lindsey](https://github.com/abk7777)**

[contributors-shield]: https://img.shields.io/github/contributors/abk7777/google-oauth2-lib.svg?style=flat-square
[contributors-url]: https://github.com/abk7777/google-oauth2-lib/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/abk7777/google-oauth2-lib.svg?style=flat-square
[forks-url]: https://github.com/abk7777/google-oauth2-lib/network/members
[issues-shield]: https://img.shields.io/github/issues/abk7777/google-oauth2-lib.svg?style=flat-square
[issues-url]: https://github.com/abk7777/google-oauth2-lib/issues
