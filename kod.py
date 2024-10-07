import smtplib
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_latest_link():
    url = 'https://www.lidl.cz/c/akcni-letak/s10008644'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    letaky = soup.find_all('a', class_='flyer')

    for letak in letaky:
        letak_url = letak['href']
        return letak_url
    
    
    
def send_email(subject, body, to_email):
    # Nastavení e-mailu
    from_email = 'bartunkova8@gmail.com'  # Nahraďte vaší adresou
    password = 'esol xoka hdhg rdpi'  # Heslo nebo aplikační heslo pro Gmail (doporučeno)

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # SMTP server a port pro Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Hlavní funkce
def main():
    # Získej nejnovější odkaz na leták
    latest_link = get_latest_link()

    if latest_link:
        # Předmět a tělo e-mailu
        subject = "Aktualizovaný leták Lidl - naprogramovano dcerou"
        body = f"Aktualizovaný odkaz na leták Lidl: {latest_link}"
        to_email = 't.bartunkova@seznam.cz'  # Nahraďte cílovou adresou

        # Odešli e-mail
        send_email(subject, body, to_email)
        print(f"E-mail byl úspěšně odeslán na {to_email}.")
    else:
        print("Nepodařilo se najít odkaz na leták.")

if __name__ == "__main__":
    main()
    