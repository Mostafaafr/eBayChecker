<h1> eBayChecker</h1>
<p> A Python script that notifies you by email when items are listed </p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
* [Usage](#usage)




<!-- ABOUT THE PROJECT -->
## About The Project

I buy Pokemon cards on eBay, and with everything in the world moving online, I found myself stuck on eBay more and more. I noticed I kept missing out on cheap cards that were listed because people were buying them within ten minutes, so I wrote a script that alerts me when cards (or anything else) within my price range are listed. 

Of course this doesn't mean I see all cards that are listed in time to buy them, but it has helped me significantly in jumping on deals I would have certainly missed.

### Built With
This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python](https://www.python.org/)
* [ebaysdk](https://github.com/timotheus/ebaysdk-python)
* [ezgmail](https://ezgmail.readthedocs.io/en/latest/)


<!-- GETTING STARTED -->
## Getting Started

1. Make an eBay developer account at [https://developer.ebay.com/] (This could take a few days to get approved).

2. Generate an API key.

3. Clone the repo
```sh
git clone https://github.com/Mostafaafr/ebayChecker.git
```
4. Install the ebaysdk by doing
```sh
pip install ebaysdk
```
and then clone the repo or download the ebaysdk files from [https://github.com/timotheus/ebaysdk-python].

5. Install the ezgmail API and generate a token using the steps found [here](https://ezgmail.readthedocs.io/en/latest/).

6. Merge  all the files from the ebaysdk and ezgmail repo's to the folder containing the eBaychecker files.

7. Enter your API key in the `ebay.yaml` file included with the ebaysdk.

8. Go into the script and replace the 'youremailhere@gmail.com' at the bottom of the script with your email adress.

9.  Finally, go into `itemNames.json` and enter the name, minimum price, maximum price, and listing type (i.e. FixedPrice or Auction) for whatever items you want to be notified about. 

10. And now you're ready to run the script as often as you like using your favorite task scheduler! I personally recommend cron if you are on linux. Keep in mind, the ebay API allows a maximum of 5000 api calls a day, and each item counts as a separate call, so make sure you are not running it too frequently. For reference, one item can be checked every 20 seconds, two every 40 seconds and so on. I recommend you schedule the task to stop whenever your normal sleeping hours are in order to save API calls. 




<!-- USAGE EXAMPLES -->
## Usage
A Youtube explanation and demonstration of the script: https://youtu.be/lKH3mCiL5x0




<!-- CONTACT -->
## Contact

Made by Mostafa Afr 

Project Link: [https://github.com/Mostafaafr/eBayChecker]
