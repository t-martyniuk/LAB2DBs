DROP TABLE IF EXISTS accounts;
CREATE TABLE accounts("Account ID" TEXT,
  "Client Name" TEXT,
  Ammount INT CHECK (Ammount >= 0)
);
INSERT INTO accounts VALUES ('YYY', 'Nik', 200);
INSERT INTO accounts VALUES ('42', 'Tanya', 500);