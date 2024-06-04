const { chromium } = require('playwright');

async function getListingDetails(page, listingUrl) {
    // Open Google Maps listing page
    await page.goto(listingUrl);

    // Wait for the page to load
    await page.waitForLoadState('networkidle');

    // Get company name
    const companyName = await page.textContent('h1');
    console.log("Company Name:", companyName);

    // Get company website
    const companyWebsite = await page.textContent('.RcCsl:nth-child(6) .fl');
    console.log("Company Website:", companyWebsite);

    // Get company phone number
    const companyPhoneNumber = await page.textContent('.RcCsl:nth-child(7) .fl');
    console.log("Company Phone Number:", companyPhoneNumber);
}

(async () => {
    // Launch browser
    const browser = await chromium.launch();
    const context = await browser.newContext();
    const page = await context.newPage();

    // Navigate to the URL
    const url = 'https://www.google.com/maps/search/it+companies+in+noida';
    await page.goto(url);

    // Wait for initial links to load
    await page.waitForSelector('.hfpxzc');

    // Get initial links
    let links = await page.$$('.hfpxzc');

    // Extract and open each link
    const listingsUrlList = [];
    for (const link of links) {
        const listingUrl = await link.getAttribute('href');
        console.log("Opening link:", listingUrl);
        listingsUrlList.push(listingUrl);
    }

    // Scrolling part currently not working. It just adds same same links 10 times in loop rather than 10 times different links in total
    for (let i = 0; i < 10; i++) { 
        // Scroll down
        await page.evaluate(() => {
            window.scrollTo(0, document.body.scrollHeight);
        });
        // Wait for some time to load content
        await page.waitForTimeout(2000); 

        // Find links and add them to the existing list
        const newLinks = await page.$$('.hfpxzc');
        if (newLinks) {
            links.push(...newLinks);
        }
    }

    console.log("Total crawled listings", listingsUrlList.length);
    console.log("Details of each listing are as follows.");

    // Get details of each listing
    for (const listingUrl of listingsUrlList) {
        await getListingDetails(page, listingUrl);
    }

    // Close browser
    await browser.close();
})();
