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

Full responsive testing was performed on mobile (412 x 869), tablet (768x1024), and desktop (1920х1080).

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


### Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page                                           | User Action                                         | Expected Result                                                                     | Pass/Fail | Comments |
| ---------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------- | --------- | -------- |
| **Navigation bar**                             |                                                     |                                                                                     |           |          |
|                                                | Click on Logo                                       | Redirection to Home page                                                            | Pass      |          |
|                                                | Click on All Products in navbar                     | Dropdown menu opens                                                                 | Pass      |          |
|                                                | Click on All products dropdown items                | Redirection to Product page with chosen sorting applied                             | Pass      |          |
|                                                | Click on navbar categories                          | Redirection to Products page with chosen category selected                          | Pass      |          |
|                                                | Click on Enquiries                                  | Redirection to Enquiries page                                                       | Pass      |          |
|                                                | Click on My Account (not logged in)                 | Register and Login shown in dropdown                                                | Pass      |          |
|                                                | Click on Shopping bag                               | Redirection to Bag page                                                             | Pass      |          |
|                                                | Click on Register                                   | Redirection Sign Up page                                                            | Pass      |          |
|                                                | Click on Login                                      | Redirection Login page                                                              | Pass      |          |
|                                                | Click on My Account (logged in)                     | Product management, My Profile and Logout options displayed in dropdown             | Pass      |          |
|                                                | Click on Product Management                         | Redirection Add Product page                                                        | Pass      |          |
|                                                | Click on My Profile                                 | Redirection Profile page                                                            | Pass      |          |
|                                                | Click on Logout                                     | Redirection Logout page                                                             | Pass      |          |
|                                                | Enter valid search terms and click search icon      | Products page containing search terms in title or description shown                 | Pass      |          |
|                                                | Enter invalid search terms and click search icon    | Products page showing 0 products found for (search terms)                           | Pass      |          |
| **Footer**                                     |                                                     |                                                                                     |           |          |
|                                                | Click on each social media icon                     | Redirection to each social media website                                            | Pass      |          |
|                                                | Click on Products link                              | Redirection Products page                                                           | Pass      |          |
|                                                | Click on Contact Us                                 | Redirection Enquiries page                                                          | Pass      |          |
|                                                | Click on Privacy Policy                             | Redirection Privacy Policy page                                                     | Pass      |          |
| **Home Page**                                  |                                                     |                                                                                     |           |          |
|                                                | Click on Shop Now button                            | Redirection Products page                                                           | Pass      |          |
| **Products Page**                              |                                                     |                                                                                     |           |          |
|                                                | Click a category in navbar                          | Correct category filter applied to products                                         | Pass      |          |
|                                                | Click on selected category in sidebar               | Category filter is removed                                                          | Pass      |          |
|                                                | Select an option from Sort By in sidebar            | Products are sorted by the selected option                                          | Pass      |          |
|                                                | Click on a product image                            | Redirection to clicked image's Product Detail page                                  | Pass      |          |
|                                                | (As superuser) Click on edit under product rating   | Redirection to Edit Product page                                                    | Pass      |          |
|                                                | (As superuser) Click on delete under product rating | Product is deleted                                                                  | Pass      |          |
|                                                | Click on category above product rating              | Clicked category filter is applied to page                                          | Pass      |          |
| **Product-detail Page**                        |                                                     |                                                                                     |           |          |
|                                                | Product with no sizes available                     | Size options are not displayed                                                      | Pass      |          |
|                                                | Product with no scents available                    | Scent options are not displayed                                                     | Pass      |          |
|                                                | Change size/scent/wax options                       | Total price is updated correctly                                                    | Pass      |          |
|                                                | Adjust quantity                                     | Total price is updated correctly                                                    | Pass      |          |
|                                                | Try to click quantity "-" button at 1 quantity      | Cannot click button                                                                 | Pass      |          |
|                                                | Try to click quantity "+" button at 99 quantity     | Cannot click button                                                                 | Pass      |          |
|                                                | Try to enter 0 for quantity                         | Minimum quantity error message displayed and quantity set to 1                      | Pass      |          |
|                                                | Try to enter 99999999 for quantity                  | Maximum quantity error message displayed and quantity set to 99                     | Pass      |          |
|                                                | Try to enter asdf for quantity                      | Unable to type letters                                                              | Pass      |          |
|                                                | Try to add to bag when bag already has 99 of option | Error message is displayed and remains at 99 in bag                                 | Pass      |          |
|                                                | Click add to bag with empty bag                     | Product/Options added to bag                                                        | Pass      |          |
|                                                | Add same product with different options to bag      | Separate entry created in bag with correct options                                  | Pass      |          |
|                                                | Click Keep Shopping button                          | Redirection to Products page                                                        | Pass      |          |
|                                                | (As superuser) Click on edit under product rating   | Redirection to Edit Product page                                                    | Pass      |          |
|                                                | (As superuser) Click on delete under product rating | Product is deleted                                                                  | Pass      |          |
| **Bag Page**                                   |                                                     |                                                                                     |           |          |
|                                                | Try to click quantity "+" button at 99 quantity     | Cannot go over 99                                                                   | Pass      |          |
|                                                | Try to click quantity "-" button at 1 quantity      | Cannot go below 1                                                                   | Pass      |          |
|                                                | Type 0 in quantity and click update                 | Product is removed from bag                                                         | Pass      |          |
|                                                | Type valid quantity and click update                | Quantity updated to entered value, prices updated correctly                         | Pass      |          |
|                                                | Click remove                                        | Product is removed from bag                                                         | Pass      |          |
|                                                | Click Keep Shopping button                          | Redirection to Products page                                                        | Pass      |          |
|                                                | Click Secure Checkout button                        | Redirection to Checkout Success page                                                | Pass      |          |
| **Checkout Page**                              |                                                     |                                                                                     |           |          |
|                                                | Try to click complete order with missing info       | Error message is displayed, cannot checkout                                         | Pass      |          |
|                                                | Try to click complete order with valid info         | Redirection to Checkout Success page, email sent                                    | Pass      |          |
|                                                | Try to enter letters in phone number field          | Allowed to complete order                                                           | Pass      |          |
|                                                | Click Adjust Bag button                             | Redirection to Bag page                                                             | Pass      |          |
|                                                | Checkout with save info checkbox checked            | Profile default info is updated                                                     | Pass      |          |
|                                                | Checkout without save info checkbox checked         | Profile default info is not updated                                                 | Pass      |          |
| **Checkout Success Page**                      |                                                     |                                                                                     |           |          |
|                                                | Access page through "my profile"                    | Back to Profile button is shown                                                     | Pass      |          |
|                                                | Click Back to Profile button                        | Redirection to Profile page                                                         | Pass      |          |
|                                                | Access through successful checkout                  | Correct order information is displayed, email is sent to entered email address      | Pass      |          |
|                                                | Click Back to Products button                       | Redirection to Products page                                                        | Pass      |          |
| **Add Product page**                           |                                                     |                                                                                     |           |          |
|                                                | Add product with valid information                  | Product is created successfully                                                     | Pass      |          |
|                                                | Try to add product with missing available scents    | Error message is displayed                                                          | Pass      |          |
|                                                | Try to add product with missing available sizes     | Error message is displayed                                                          | Pass      |          |
|                                                | Try to add product with missing available wax       | Error message is displayed                                                          | Pass      |          |
|                                                | Try to add product with invalid price               | Error message is displayed                                                          | Pass      |          |
|                                                | Try to add product with no rating                   | Product created successfully, rating is not displayed on product page               | Pass      |          |
| **Edit Product page**                          |                                                     |                                                                                     |           |          |
|                                                | Click edit on a product                             | Information is automatically filled                                                 | Pass      |          |
|                                                | Click cancel button                                 | Product is not updated                                                              | Pass      |          |
|                                                | Update product with valid information               | Product is updated successfully                                                     | Pass      |          |
|                                                | Try to update product with missing available scents | Error message is displayed                                                          | Pass      |          |
|                                                | Try to update product with missing available sizes  | Error message is displayed                                                          | Pass      |          |
|                                                | Try to update product with missing available wax    | Error message is displayed                                                          | Pass      |          |
|                                                | Try to update product with invalid price            | Error message is displayed                                                          | Pass      |          |
|                                                | Try to update product with no rating                | Product created successfully, rating is not displayed on product page               | Pass      |          |
| **Profile page**                               |                                                     |                                                                                     |           |          |
|                                                | Account with order history                          | Order history is present                                                            | Pass      |          |
|                                                | Account without order history                       | Order history is empty                                                              | Pass      |          |
|                                                | Account with saved default details                  | Details are automatically filled                                                    | Pass      |          |
|                                                | Account without saved default details               | Details are empty                                                                   | Pass      |          |
|                                                | Click Update Information button                     | Details are saved                                                                   | Pass      |          |
| **Enquiries page**                             |                                                     |                                                                                     |           |          |
|                                                | Click send message with missing required info       | Error messages are displayed                                                        | Pass      |          |
|                                                | Click send message with valid info                  | Form successfully submitted                                                         | Pass      |          |
| **Logout page**                                |                                                     |                                                                                     |           |          |
|                                                | Click Sign Out button                               | User is logged out and redirected to index page, notification displayed             | Pass      |          |
|                                                | Click cancel button                                 | Redirected to Index page and user stays logged in                                   | Pass      |          |
| **Login page**                                 |                                                     |                                                                                     |           |          |
|                                                | Leave username blank and try to Submit              | A required message popped up                                                        | Pass      |          |
|                                                | Leave password blank and try to Submit              | A required message popped up                                                        | Pass      |          |
|                                                | Enter valid username and password and try to Submit | Logged in successfully and notification displayed                                   | Pass      |          |
|                                                | Enter valid email and password and try to Submit    | Logged in successfully and notification displayed                                   | Pass      |          |
| **Sign Up page**                               |                                                     |                                                                                     |           |          |
|                                                | Leave email blank and try to Submit                 | A required message popped up                                                        | Pass      |          |
|                                                | Leave username blank and try to Submit              | A required message popped up                                                        | Pass      |          |
|                                                | Leave password blank and try to Submit              | A required message popped up                                                        | Pass      |          |
|                                                | Leave password (again) blank and try to Submit      | A required message popped up                                                        | Pass      |          |
|                                                | Enter invalid email address                         | A valid email reminder message popped up                                            | Pass      |          |
|                                                | Enter a username that is too short                  | A valid username message popped up                                                  | Pass      |          |
|                                                | Enter a password similar to the username            | An error message is displayed                                                       | Pass      |          |
|                                                | Enter a common password                             | An error message is displayed                                                       | Pass      |          |
|                                                | Enter passwords that do not match                   | An error message is displayed                                                       | Pass      |          |
|                                                | Enter a password containing only numbers            | An error message is displayed                                                       | Pass      |          |
|                                                | Enter a passwords that is less than 8 characters    | An error message is displayed                                                       | Pass      |          |
|                                                | Try to sign up with an existing user/email          | An error message is displayed                                                       | Pass      |          |
|                                                | Enter valid information                             | Successful, user redirected to Home page and logged in                              | Pass      |          |
| **404 page**                                   |                                                     |                                                                                     |           |          |
|                                                | Click Back to Homepage button                       | User is redirected to the Home page                                                 | Pass      |          |
|                                                | Click Browse Products button                        | User is redirected to the Products page                                             | Pass      |          |
| **500 page**                                   |                                                     |                                                                                     |           |          |
|                                                | Unable to test                                      | Interactive content same as 404 page, so Pass expected                              | Pass      |          |
