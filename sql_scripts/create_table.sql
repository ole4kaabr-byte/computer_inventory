-- Создание таблицы Equipment, если она еще не существует
CREATE TABLE IF NOT EXISTS Equipment (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Type VARCHAR(50),
    Brand VARCHAR(50),
    Model VARCHAR(50),
    SerialNumber VARCHAR(100) UNIQUE,
    Location VARCHAR(50),
    Status VARCHAR(20),
    PurchaseDate DATE,
    WarrantyPeriod INTEGER,
    ResponsiblePerson VARCHAR(50)
);
