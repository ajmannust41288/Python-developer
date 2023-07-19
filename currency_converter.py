# import requests
#
# def get_exchange_rate():
#     # This function fetches the latest exchange rate of 1 USD to PKR from an API.
#     try:
#         response = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=PKR")
#         data = response.json()
#         exchange_rate = data["rates"]["PKR"]
#         return exchange_rate
#     except requests.exceptions.RequestException as e:
#         print("Error fetching exchange rate:", e)
#         return None
#
# def dollar_to_pkr(amount):
#     # This function converts the given amount from USD to PKR using the latest exchange rate.
#     exchange_rate = get_exchange_rate()
#     if exchange_rate is not None:
#         return amount * exchange_rate
#     else:
#         return None
#
# if __name__ == "__main__":
#     print("Welcome to Dollar to PKR Exchange Rates Converter!")
#
#     # Input amount in USD
#     try:
#         amount_in_usd = float(input("Enter the amount in USD to convert to PKR: "))
#     except ValueError:
#         print("Invalid input. Please enter a valid number for the amount.")
#         exit(1)
#
#     # Perform conversion
#     amount_in_pkr = dollar_to_pkr(amount_in_usd)
#
#     if amount_in_pkr is not None:
#         # Display the result
#         print(f"{amount_in_usd:.2f} USD is equivalent to {amount_in_pkr:.2f} PKR.")
#     else:
#         print("Unable to perform the conversion. Please try again later.")
# ==========================
#========================# ================currency convertor
# def currency_converter(amount, exchange_rate):
#     # This function takes an amount in one currency and an exchange rate
#     # and returns the equivalent amount in another currency.
#     return amount * exchange_rate
#
# # Example usage:
# # Convert 100 USD to EUR using an exchange rate of 0.85
# amount_in_usd = 100
# exchange_rate_usd_to_eur = 0.85
# amount_in_eur = currency_converter(amount_in_usd, exchange_rate_usd_to_eur)
# print(f"{amount_in_usd} USD is equivalent to {amount_in_eur} EUR.")
#=============================================part 2
# def currency_converter(amount, exchange_rate):
#     # This function takes an amount in one currency and an exchange rate
#     # and returns the equivalent amount in another currency.
#     return amount * exchange_rate
#
#
# if __name__ == "__main__":
#     print("Welcome to Currency Converter!")
#
#     # Input amount and currency code
#     try:
#         amount = float(input("Enter the amount to convert: "))
#         source_currency = input("Enter the source currency code: ").upper()
#         target_currency = input("Enter the target currency code: ").upper()
#     except ValueError:
#         print("Invalid input. Please enter a valid number for the amount.")
#         exit(1)
#
#     # Exchange rates for conversion (can be fetched from an API or database in a real project)
#     exchange_rates = {
#         "USD": 0.85,
#         "EUR": 1.18,
#         "GBP": 1.39,
#         # Add more currencies and their exchange rates here
#     }
#
#     # Check if currencies are supported
#     if source_currency not in exchange_rates or target_currency not in exchange_rates:
#         print("Unsupported currency. Please enter valid currency codes.")
#         exit(1)
#
#     # Perform conversion
#     exchange_rate = exchange_rates[target_currency] / exchange_rates[source_currency]
#     converted_amount = currency_converter(amount, exchange_rate)
#
#     # Display the result
#     print(f"{amount:.2f} {source_currency} is equivalent to {converted_amount:.2f} {target_currency}.")
#==========================================part3 of this project
# import requests
#
# def get_exchange_rate():
#     # This function fetches the latest exchange rate of 1 USD to PKR from an API.
#     try:
#         response = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=PKR")
#         data = response.json()
#         exchange_rate = data["rates"]["PKR"]
#         return exchange_rate
#     except requests.exceptions.RequestException as e:
#         print("Error fetching exchange rate:", e)
#         return None
#
# def dollar_to_pkr(amount):
#     # This function converts the given amount from USD to PKR using the latest exchange rate.
#     exchange_rate = get_exchange_rate()
#     if exchange_rate is not None:
#         return amount * exchange_rate
#     else:
#         return None
#
# if __name__ == "__main__":
#     print("Welcome to Dollar to PKR Exchange Rates Converter!")
#
#     # Input amount in USD
#     try:
#         amount_in_usd = float(input("Enter the amount in USD to convert to PKR: "))
#     except ValueError:
#         print("Invalid input. Please enter a valid number for the amount.")
#         exit(1)
#
#     # Perform conversion
#     amount_in_pkr = dollar_to_pkr(amount_in_usd)
#
#     if amount_in_pkr is not None:
#         # Display the result
#         print(f"{amount_in_usd:.2f} USD is equivalent to {amount_in_pkr:.2f} PKR.")
#     else:
#         print("Unable to perform the conversion. Please try again later.")
#==============================================================================part 4
# import requests
#
# def get_exchange_rates():
#     # This function fetches the latest exchange rates from an API for all currencies to PKR.
#     try:
#         response = requests.get("https://api.exchangeratesapi.io/latest?base=PKR")
#         data = response.json()
#         exchange_rates = data["rates"]
#         return exchange_rates
#     except requests.exceptions.RequestException as e:
#         print("Error fetching exchange rates:", e)
#         return None
#
# def convert_currency_to_pkr(amount, exchange_rate):
#     # This function converts the given amount to PKR using the provided exchange rate.
#     return amount * exchange_rate
#
# if __name__ == "__main__":
#     print("Welcome to All Currency to PKR Exchange Rates Converter!")
#
#     # Input amount and currency code
#     try:
#         amount = float(input("Enter the amount to convert: "))
#         source_currency = input("Enter the source currency code: ").upper()
#     except ValueError:
#         print("Invalid input. Please enter a valid number for the amount.")
#         exit(1)
#
#     # Fetch all exchange rates to PKR
#     exchange_rates = get_exchange_rates()
#
#     if exchange_rates is not None:
#         # Check if source currency is supported
#         if source_currency not in exchange_rates:
#             print("Unsupported currency. Please enter a valid currency code.")
#             exit(1)
#
#         # Perform conversion
#         exchange_rate = exchange_rates[source_currency]
#         amount_in_pkr = convert_currency_to_pkr(amount, exchange_rate)
#
#         # Display the result
#         print(f"{amount:.2f} {source_currency} is equivalent to {amount_in_pkr:.2f} PKR.")
#     else:
#         print("Unable to fetch exchange rates. Please try again later.")
