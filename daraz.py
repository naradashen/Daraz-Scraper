from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_daraz_deals():
    url = "https://www.daraz.lk/#hp-categories"
    total_scraped_items = 0

    # Configure Chrome webdriver
    service = Service('/usr/local/bin/chromedriver')  # Update with the path to your chromedriver executable
    service.start()
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url)

        while True:
            # Find product containers
            product_containers = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="card-jfy-item-desc"]')))

            # Debugging: Print the number of product containers found
            print("Number of product containers found:", len(product_containers))
            total_scraped_items += len(product_containers)

            # Iterate over product containers and scrape the information
            for container in product_containers:
                # Extract product name
                product_name = container.find_element(By.XPATH, './/div[@class="card-jfy-title"]/span[@class="title"]').text

                # Extract current price
                current_price = container.find_element(By.XPATH, './/div[@class="hp-mod-price"]/div[@class="hp-mod-price-first-line"]/span[@class="price"]').text

                # Extract discounted price
                discounted_price_element = container.find_elements(By.XPATH, './/div[@class="hp-mod-price"]/div[@class="hp-mod-price-second-line"]//span[@class="price"]')
                discounted_price = discounted_price_element[0].text if discounted_price_element else "N/A"

                # Extract discount percentage
                discount_percentage_element = container.find_elements(By.XPATH, './/div[@class="hp-mod-price"]/div[@class="hp-mod-price-second-line"]/span[@class="hp-mod-discount align-left"]')
                discount_percentage = discount_percentage_element[0].text.strip() if discount_percentage_element else "0"

                # Print the product info with space between each product
                print(f"Product: {product_name},    Current Price: {current_price},    Discounted Price: {discounted_price},    Discount Percentage: {discount_percentage}\n")

            # Find and click the "Load More" button
            load_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'J_LoadMoreButton')))
            load_more_button.click()

            # Wait for the products to load
            WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'card-jfy-loading')))

            # Check if no more products are loaded
            new_product_containers = driver.find_elements(By.XPATH, '//div[@class="card-jfy-item-desc"]')
            if len(new_product_containers) == len(product_containers):
                break

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()
        service.stop()
        print(f"Total scraped items: {total_scraped_items}")

scrape_daraz_deals()
