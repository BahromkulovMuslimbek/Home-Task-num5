## Task num 1
# def count_words_in_file(file_name):
#     try:
#         file = open(file_name, 'r', encoding='utf-8')
#         with file:
#             return len(file.read().split())
#     except FileNotFoundError:
#         return " Fayl topilmadi"


# file_name = "oquvchi.txt"
# print(f"'{file_name}' faylidagi sozlar soni: {count_words_in_file (file_name)}")




# # Task num 2
# def find_longest_word_in_file(file_name):
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             words = file.read().split()
#             if not words:
#                 return "Faylda sozlar topilmadi"
#             longest_word = max(words, key=len)
#             return longest_word
#     except FileNotFoundError:
#         return " Fayl topilmadi"
#     except Exception as e:
#         return f"Hato yuz berdi: {e}"


# file_name = "oquvchi.txt"
#print(f"'{file_name}' faylidagi eng uzun soz: {find_longest_word_in_file (file_name)}")




# # Task num 3
# def find_disruption(numbers):
#     for i in range(1, len(numbers)):
#         if numbers[i] < numbers[i - 1]:
#             return numbers[i]
#     return "Royxat osish tartibida."


# numbers = [1, 2, 4, 5, 6, 8, 7]
# print(f"Buzilgan raqam: {find_disruption(numbers)}")




# # Task num 4
# emails = ["ali@gmail.com", 55, "asad@gmail.com", 'Assalomu aleykum', "hasan@gmail.com", 3.09, "fotima@gmail.com"]

# gmail_emails = [str(email) for email in emails if isinstance(email, str) and email.endswith("@gmail.com")]
# sorted_gmail_emails = sorted(gmail_emails)

# print('Gmaillar: ')
# for email in sorted_gmail_emails:
#     print(email)
