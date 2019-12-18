GBP = {
    "table": "A",
    "currency": "funt szterling",
    "code": "GBP",
    "rates": [
        {
            "no": "209/A/NBP/2019",
            "effectiveDate": "2019-10-28",
            "mid": 4.9504
        },
        {
            "no": "210/A/NBP/2019",
            "effectiveDate": "2019-10-29",
            "mid": 4.9487
        },
        {
            "no": "211/A/NBP/2019",
            "effectiveDate": "2019-10-30",
            "mid": 4.9472
        },
        {
            "no": "212/A/NBP/2019",
            "effectiveDate": "2019-10-31",
            "mid": 4.9405
        }
    ]
}
print("Data", "\t\t", "Kurs")
print("========================")
pom=-1
for m in range (0, len(GBP["rates"])):
    pom+=1
    print(GBP["rates"][pom]["effectiveDate"], "\t\t", GBP["rates"][pom]["mid"])
