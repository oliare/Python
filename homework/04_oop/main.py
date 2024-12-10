# task 1
class Passport:

    def __init__(self, firstName, lastName, middleName, citizenship, birth, sex, number):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
        self.citizenship = citizenship
        self.birth = birth
        self.sex = sex
        self.number = number
    
    def getNumber(self):
        return self.number

    def setNumber(self, value):
        self.number = value

    def showInfo(self):
        fullName = f"{self.lastName} {self.firstName} {self.middleName}"
        print(f"Full name: {fullName}\nCitizenship: {self.citizenship}\nBirth date: {self.birth}\nSex: {self.sex}\nNumber: {self.number}")

    def __str__(self) -> str:
        fullName = f"{self.lastName} {self.firstName} {self.middleName}"
        return f"Full name: {fullName}\nCitizenship: {self.citizenship}\nBirth date: {self.birth}\nSex: {self.sex}\nNumber: {self.number}"
    
    def __del__(self):
        print("--- Data cleared ---")


class ForeignPassport(Passport):

    def __init__(self, firstName, lastName, middleName, citizenship, birth, sex, pnumber, fpnumber):
        super().__init__(firstName, lastName, middleName, citizenship, birth, sex, pnumber)
        self.fpnumber = fpnumber
        self.visas = []
    
    def addVisa(self, visa, issued, expired):
        self.visas.append({"Visa": visa, "Issued": issued, "Expired": expired})

    def removeVisa(self, visa):
        self.visas = [v for v in self.visas if v != visa]

    def showInfo(self):
        super().showInfo()
        print(f"F-passport number: {self.fpnumber}\nVisas:")
        for visa in self.visas:
            print(f"\tVisa: {visa['Visa']} (issued: {visa['Issued']}, expired: {visa['Expired']})")

    def __str__(self):
        passport = super().__str__()
        visas = '\n'.join([f"\tVisa: {visa['Visa']} (issued: {visa['Issued']}, expired: {visa['Expired']})" for visa in self.visas])
        return (f"{passport}\nF-passport number: {self.fpnumber}\nVisas:\n{visas}")

print("\n\t>> Passport <<")
passport = Passport("Biba", "Cool", "Coolest", "USA", "27.04.2005", "Female", "192837")

passport.showInfo()

print("\n\t>> Foreign passport <<")
fpassport = ForeignPassport("Boba", "Bobas", "Bobastest", "UA", "20.01.2000", "Male", "1234569", "AA1234567")

fpassport.addVisa("France", "2024-01-01", "2024-12-31")
fpassport.addVisa("Japan", "2025-03-15", "2025-09-15")
fpassport.removeVisa("France")
print(fpassport)


# task 2
class TempConverter:

    count = 0
    const = 32

    @staticmethod
    def CtoF(c):
        TempConverter.count += 1
        return c * 1.8 + TempConverter.const

    @staticmethod
    def FtoC(f):
        TempConverter.count += 1
        return (f - TempConverter.const) * 0.5
   
    @staticmethod
    def getCount(): return TempConverter.count


print("To F*:", TempConverter.CtoF(1))
print("To C*:", TempConverter.FtoC(1))
print("Count of convertation:", TempConverter.getCount())