# Testing

Return to the [README.md](README.md) file.

## CONTENTS

- [AUTOMATED TESTING](#automated-testing)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
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

### JS / jQuery

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