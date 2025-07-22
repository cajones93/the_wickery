# Testing

Return to the [README.md](README.md) file.

## CONTENTS

- [AUTOMATED TESTING](#automated-testing)
  - [HTML](#html)
  - [CSS](#css)
  - [JS and jQuery](#js-and-jquery)
  - [Python](#python)
  - [Lighthouse](#lighthouse)
- [MANUAL TESTING](#manual-testing)
  - [Responsiveness](#responsiveness)
  - [Defensive Programming](#defensive-programming)
  - [User Story Testing](#user-story-testing)
- [SOLVED BUGS](#solved-bugs)

## AUTOMATED TESTING

### HTML

The recommended [HTML W3C Validator](https://validator.w3.org) was used to validate all HTML files.
The 404 page was tested by direct input because the validator received a 404 error.

| Page             | Pass / Error    | Notes          |
| ---------------- | --------------- |--------------- |
| Home             | Pass: No Errors |                |
| Products         | Pass: No Errors |                |
| Product-Detail   | Pass: No Errors |                |
| Add Product      | Error           | "Duplicate attribute id" from page source, but not shown in devtools html or vscode | 
| Edit Product     | Error           | "The value of the for attribute of the label element must be the ID of a non-hidden form control" Label is only shown when form control is shown. |
| Profile          | Pass: No Errors |
| Enquiry          | Pass: No Errors |
| Privacy Policy   | Pass: No Errors |
| Checkout         | Pass: No Errors |
| Checkout Success | Pass: No Errors |
| Bag              | Pass: No Errors |
| 404              | Pass: No Errors |
| 500              | Pass: No Errors |

### CSS

The recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) was used to validate my CSS file.

| Page         | Notes           |
| --------     | --------------- |
| base.css     | Pass: No Errors |
| profile.css  | Pass: No Errors |
| checkout.css | Pass: No Errors |

### JS and jQuery

jQuery was validated using [jQuery Validator](https://www.utilities-online.info/jquery-validator).

| Page                  | Notes           |
| --------              | --------------- |
| checkout.html         | Pass: No Errors |
| privacy_policy.html   | Pass: No Errors |
| bag.html              | Pass: No Errors |
| products.html         | Pass: No Errors |
| add_product.html      | Pass: No Errors |
| edit_product.html     | Pass: No Errors |
| product_detail.html   | Pass: No Errors |
| profile.html          | Pass: No Errors |

### Python

The recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) was used to validate all of my Python files.
The only errors returned were 'line too long' errors which have been excluded from the notes in below tables.

#### Validation For The_Wickery App

| File        | Notes           |
| ----------- | --------------- |
| settings.py | Pass: No Errors |
| urls.py     | Pass: No Errors |

#### Validation For Home App

| File     | Notes           |
| -------- | --------------- |
| urls.py  | Pass: No Errors |
| views.py | Pass: No Errors |

#### Validation For Bag App

| File          | Notes           |
| ---------     | --------------- |
| urls.py       | Pass: No Errors |
| views.py      | Pass: No Errors |
| contexts.py   | Pass: No Errors |

#### Validation For Checkout App

| File                  | Notes           |
| ---------             | --------------- |
| forms.py              | Pass: No Errors |
| models.py             | Pass: No Errors |
| signals.py            | Pass: No Errors |
| urls.py               | Pass: No Errors |
| views.py              | Pass: No Errors |
| webhook_handler.py    | Pass: No Errors |
| webhooks.py           | Pass: No Errors |

#### Validation For Enquiries App

| File          | Notes           |
| ---------     | --------------- |
| urls.py       | Pass: No Errors |
| views.py      | Pass: No Errors |
| forms.py      | Pass: No Errors |
| models.py     | Pass: No Errors |

#### Validation For Products App

| File          | Notes           |
| ---------     | --------------- |
| urls.py       | Pass: No Errors |
| views.py      | Pass: No Errors |
| forms.py      | Pass: No Errors |
| models.py     | Pass: No Errors |
| widgets.py    | Pass: No Errors |

#### Validation For Profiles App

| File          | Notes           |
| ---------     | --------------- |
| urls.py       | Pass: No Errors |
| views.py      | Pass: No Errors |
| forms.py      | Pass: No Errors |
| models.py     | Pass: No Errors |

### Lighthouse

All pages were checked with lighthouse to identify any issues.
Best Practices is impacted by the stripe cookie which lighthouse doesn't seem to like.


| Page              | Screenshot                                                                        |
| --------------    | ----------------------------------------------------------------------------------|
| Home              | ![screenshot](documentation/testing/lighthouse/lighthouse-home.png)               |
| Products          | ![screenshot](documentation/testing/lighthouse/lighthouse-products.png)           |
| Product Detail    | ![screenshot](documentation/testing/lighthouse/lighthouse-product-detail.png)     |
| Add Product       | ![screenshot](documentation/testing/lighthouse/lighthouse-add-product.png)        |
| Edit Product      | ![screenshot](documentation/testing/lighthouse/lighthouse-edit-product.png)       |
| Bag               | ![screenshot](documentation/testing/lighthouse/lighthouse-bag.png)                |
| Checkout          | ![screenshot](documentation/testing/lighthouse/lighthouse-checkout.png)           |
| Checkout Success  | ![screenshot](documentation/testing/lighthouse/lighthouse-checkout-success.png)   |
| Profile           | ![screenshot](documentation/testing/lighthouse/lighthouse-profile.png)            |
| Enquiries         | ![screenshot](documentation/testing/lighthouse/lighthouse-enquiries.png)          |
| Privacy Policy    | ![screenshot](documentation/testing/lighthouse/lighthouse-privacy-policy.png)     |
| Login             | ![screenshot](documentation/testing/lighthouse/lighthouse-login.png)              |
| Sign Up           | ![screenshot](documentation/testing/lighthouse/lighthouse-sign-up.png)            |
| Logout            | ![screenshot](documentation/testing/lighthouse/lighthouse-logout.png)             |

## MANUAL TESTING

### Responsiveness

Full responsive testing was performed on mobile, tablet, and desktop following devices:

| Page              | Size      | Screenshot                                                                            |
| -----------       | -------   | ----------------------------------------------------------------------------------    |
| Home              | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/home-desk.png)             |
| Home              | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/home-tab.png)               |
| Home              | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/home-mob.png)               |
| Products          | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/products-desk.png)         |
| Products          | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/products-tab.png)           |
| Products          | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/products-mob.png)           |
| Product Detail    | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/product-detail-desk.png)   |
| Product Detail    | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/product-detail-tab.png)     |
| Product Detail    | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/product-detail-mob.png)     |
| Add Product       | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/add-product-desk.png)      |
| Add Product       | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/add-product-tab.png)        |
| Add Product       | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/add-product-mob.png)        |
| Edit Product      | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/edit-product-desk.png)     |
| Edit Product      | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/edit-product-tab.png)       |
| Edit Product      | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/edit-product-mob.png)       |
| Checkout          | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/checkout-desk.png)         |
| Checkout          | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/checkout-tab.png)           |
| Checkout          | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/checkout-mob.png)           |
| Checkout Success  | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/checkout-success-desk.png)  |
| Checkout Success  | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/checkout-success-tab.png)   |
| Checkout Success  | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/checkout-success-mob.png)   |
| Enquiries         | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/enquiries-desk.png)        |
| Enquiries         | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/enquiries-tab.png)          |
| Enquiries         | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/enquiries-mob.png)          |
| Privacy Policy    | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/policy-desk.png)           |
| Privacy Policy    | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/privacy-tab.png)            |
| Privacy Policy    | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/policy-mob.png)             |
| Bag               | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/bag-desk.png)              |
| Bag               | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/bag-tab.png)                |
| Bag               | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/bag-mob.png)                |
| Login             | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/login-desk.png)            |
| Login             | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/login-tab.png)              |
| Login             | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/login-mob.png)              |
| Sign Up           | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/sign-up-desk.png)          |
| Sign Up           | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/sign-up-tab.png)            |
| Sign Up           | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/sign-up-mob.png)            |
| Logout            | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/logout-desk.png)           |
| Logout            | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/logout-tab.png)             |
| Logout            | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/logout-mob.png)             |
| 404               | Desktop   | ![screenshot](documentation/testing/responsiveness/desktop/404-desk.png)              |
| 404               | Tablet    | ![screenshot](documentation/testing/responsiveness/tablet/404-tab.png)                |
| 404               | Mobile    | ![screenshot](documentation/testing/responsiveness/mobile/404-mob.png)                |

