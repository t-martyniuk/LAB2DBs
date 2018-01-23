DROP TABLE IF EXISTS flights;
CREATE TABLE flights("Booking ID" TEXT,
  "Client Name" TEXT,
  "Fly Number" TEXT,
  "From" TEXT,
  "To" TEXT,
  "Date" DATE
);
INSERT INTO flights VALUES ('XXX', 'Nik', 'KLM 1382', 'KBP', 'AMS', '01/05/2015');