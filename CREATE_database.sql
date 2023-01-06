create table ulogazaposlenika(
    IDUlogaZaposlenika SERIAL PRIMARY KEY,
    Naziv TEXT NOT NULL
);

insert into ulogazaposlenika (naziv)
values 
('developer'),
('HR'),
('PM'),
('Support');

create table status(
    IDStatus SERIAL PRIMARY KEY,
    Status TEXT NOT NULL
);

insert into status (Status)
values
('U uredu'),
('Od kuće'),
('Godisnji'),
('Bolovanje'),
('Odsutan');


create table zaposlenik(
    ZaposlenikID SERIAL PRIMARY KEY,
    Ime_i_prezime TEXT NOT NULL,
    Broj_mobitela TEXT NOT NULL,
    IDUlogaZaposlenika INT REFERENCES ulogazaposlenika(IDUlogaZaposlenika) ON UPDATE CASCADE ON DELETE RESTRICT,
    Satnica FLOAT,
    Lozinka TEXT NOT NULL,
    Email TEXT,
    IDStatus INT REFERENCES status(IDStatus) ON UPDATE CASCADE ON DELETE RESTRICT,
    GodisnjiOdmorUkupno INT NOT NULL,
    GodisnjiOdmorPreostaloDana INT,
    RadnoVrijeme FLOAT NOT NULL
);

insert into zaposlenik(Ime_i_prezime, Broj_mobitela, IDUlogaZaposlenika, Satnica, Lozinka, Email, IDStatus, GodisnjiOdmorUkupno, GodisnjiOdmorPreostaloDana, RadnoVrijeme)
values 
('Ivan Ivic', '', 1, 35, 'jastuk54', 'ivan@email.com', 1, 10, 10, 8),
('Ivana Trajnk', '+3859345745', 1, 40, 'sifra11', 'ivana@email.com', 1, 10, 6, 8),
('Petar Peric', '', 1, 33, 'password', 'petar@email.com', 1, 10, 5, 8),
('Jura Klobuk', '3859764456', 1, 37, 'teskasifra14', 'jura@email.com', 1, 10, 10, 6),
('Boris Knezevic', '385907654', 1, 44, 'hehepass123', 'boris@email.com', 1, 20, 11, 8),
('Marija Cicak', '', 1, 36, 'crniRex151230', 'marija@email.com', 1, 20, 3, 4);
('a', '', 1, 36, 'a', 'marija@email.com', 1, 20, 3, 4);



create table bolovanje(
    IDBolovanja SERIAL PRIMARY KEY,
    ZaposlenikID INT REFERENCES zaposlenik(ZaposlenikID) ON UPDATE CASCADE ON DELETE RESTRICT,
    Pocetak TIMESTAMP,
    Kraj TIMESTAMP
);


create table godisnjiodmor(
    IDGodisnjeg SERIAL PRIMARY KEY,
    ZaposlenikID INT REFERENCES zaposlenik(ZaposlenikID) ON UPDATE CASCADE ON DELETE RESTRICT,
    Pocetak TIMESTAMP,
    Kraj TIMESTAMP
);

create table worklogentry(
    IDEntry SERIAL PRIMARY KEY,
    ZaposlenikID INT REFERENCES zaposlenik(ZaposlenikID) ON UPDATE CASCADE ON DELETE RESTRICT,
    Datum DATE,
    OdradeniSati FLOAT
);


create table obracun(
    IDObracun SERIAL PRIMARY KEY,
    ZaposlenikID INT REFERENCES zaposlenik(ZaposlenikID) ON UPDATE CASCADE ON DELETE RESTRICT,
    UkupnoOdradeniSati FLOAT,
    SatnicaZaposlenika FLOAT,
    IznosZaIsplatu FLOAT
);


-- drop table zaposlenik, ulogazaposlenika, status, bolovanje, godisnjiodmor, worklogentry, obracun;