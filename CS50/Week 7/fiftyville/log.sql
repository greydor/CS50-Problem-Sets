-- Crime info --
-- The theft took place on July 28, 2021 at 10:15 am.
-- Location: Humphrey Street bakery.


-- Find description of the crime.
SELECT description FROM crime_scene_reports WHERE description LIKE "%duck%";
-- Decription: Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
--  Interviews were conducted today with three witnesses who were present at the time –
--  each of their interview transcripts mentions the bakery.

-- Find interviews of the crime.
SELECT name, transcript FROM interviews WHERE transcript LIKE "%bakery%";
--Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--          If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
--Eugene  | I don't know the thief's name, but it was someone I recognized.
--          Earlier this morning, before I arrived at Emma's bakery,
--          I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
--Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
--          In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--          The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- Identify suspects based on parking lot security logs.
SELECT people.name FROM people
WHERE people.license_plate IN
    (SELECT license_plate FROM bakery_security_logs
    WHERE year=2021 AND month=7 AND day=28 AND hour=10
    AND minute BETWEEN 15 AND 25 AND activity LIKE "exit");
--Suspects: Vanessa, Barry, Iman, Sofia, Luca, Diana, Kelsey, Bruce

-- Narrow suspects from the above list who also withdrew money from Leggett Street ATM.
SELECT name FROM people WHERE id IN
    (SELECT person_id FROM bank_accounts WHERE account_number IN
        (SELECT account_number FROM atm_transactions
        WHERE year=2021 AND month=7 AND day=28
        AND atm_location LIKE "Leggett Street" AND transaction_type LIKE "Withdraw"))
AND name IN ("Vanessa", "Barry", "Iman", "Sofia", "Luca", "Diana", "Kelsey", "Bruce");
--Suspects: Iman, Luca, Diana, Bruce

-- Narrow suspects from the above list who also placed a call <1 min.
SELECT name FROM people WHERE phone_number in
    (SELECT caller FROM phone_calls WHERE year=2021 AND month=7 AND day=28 AND duration <60)
AND name IN ("Iman", "Luca", "Diana", "Bruce");
--Suspects: Diana, Bruce

-- Find fiftyville airport id
SELECT * FROM airports WHERE city LIKE "Fiftyville";
--+----+--------------+-----------------------------+------------+
--| id | abbreviation |          full_name          |    city    |
--+----+--------------+-----------------------------+------------+
--| 8  | CSF          | Fiftyville Regional Airport | Fiftyville |
--+----+--------------+-----------------------------+------------+


-- Find earliest flght out the day after the heist.
SELECT * FROM flights WHERE year=2021 AND month=7 AND day=29 AND origin_airport_id=8 ORDER BY hour, minute ASC;
--+----+-------------------+------------------------+------+-------+-----+------+--------+
--| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
--+----+-------------------+------------------------+------+-------+-----+------+--------+
--| 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     |

-- Narrow suspects from the above list who also left on the earliest flight.
SELECT name FROM people WHERE passport_number IN
    (SELECT passport_number FROM passengers WHERE flight_id=36)
AND name IN ("Diana", "Bruce");
--Suspect: Bruce

--Find flight destination
SELECT city FROM airports WHERE id IN
    (SELECT destination_airport_id FROM flights WHERE id=36);
--Destination: New York City

-- Find info about Bruce
SELECT * FROM people WHERE name LIKE "Bruce";
--+--------+-------+----------------+-----------------+---------------+
--|   id   | name  |  phone_number  | passport_number | license_plate |
--+--------+-------+----------------+-----------------+---------------+
--| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
--+--------+-------+----------------+-----------------+---------------+

-- Find accomplice
SELECT name FROM people WHERE phone_number in
    (SELECT receiver FROM phone_calls WHERE year=2021 AND month=7 AND day=28 AND duration <60 AND caller="(367) 555-5533");
--Accomplice: Robin

