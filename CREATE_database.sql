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
('Ivana Trajnk', '+3859345745', 2, 40, 'sifra11', 'ivana@email.com', 1, 10, 6, 8),
('Petar Peric', '', 1, 33, 'password', 'petar@email.com', 1, 10, 5, 8),
('Jura Klobuk', '3859764456', 3, 37, 'teskasifra14', 'jura@email.com', 1, 10, 10, 6),
('Boris Knezevic', '385907654', 4, 44, 'hehepass123', 'boris@email.com', 1, 20, 11, 8),
('Marija Cicak', '', 1, 36, 'crniRex151230', 'marija@email.com', 1, 20, 3, 4),
('a', '', 1, 36, 'a', 'marija@email.com', 1, 20, 3, 4);




create table bolovanje(
    IDBolovanja SERIAL PRIMARY KEY,
    ZaposlenikID INT REFERENCES zaposlenik(ZaposlenikID) ON UPDATE CASCADE ON DELETE RESTRICT,
    Pocetak DATE,
    Kraj DATE
);


create or replace function updateBolovanje()
    returns trigger as $$
        begin
            update zaposlenik set idstatus=4 where zaposlenikid= (select zaposlenikid from bolovanje where idbolovanja = (select idbolovanja from bolovanje order by idbolovanja desc limit 1));
            return new;
        end;
    $$
    language plpgsql;

create trigger change_bolovanje
    after insert or update on bolovanje
    for each row
    execute procedure updateBolovanje();

insert into bolovanje (zaposlenikid, pocetak, kraj)
values (1, '20-11-2013'::DATE,'20-12-2023'::DATE);



create table godisnjiodmor(
    IDGodisnjeg SERIAL PRIMARY KEY,
    ZaposlenikID INT REFERENCES zaposlenik(ZaposlenikID) ON UPDATE CASCADE ON DELETE RESTRICT,
    Pocetak TIMESTAMP,
    Kraj TIMESTAMP
);


create or replace function updateGodisnji()
    returns trigger as $$
        begin
            update zaposlenik set idstatus=3 where zaposlenikid= (select zaposlenikid from godisnjiodmor where idgodisnjeg = (select idgodisnjeg from godisnjiodmor order by idgodisnjeg desc limit 1));
            return new;
        end;
    $$
    language plpgsql;


create trigger change_godisnji
    after insert or update on godisnjiodmor
    for each row
    execute procedure updateGodisnji();

insert into godisnjiodmor (zaposlenikid, pocetak, kraj) 
values (2, '31-01-2023'::TIMESTAMP, '04-02-2023'::TIMESTAMP);


create table worklogentry(
    IDEntry SERIAL PRIMARY KEY,
    ZaposlenikID INT REFERENCES zaposlenik(ZaposlenikID) ON UPDATE CASCADE ON DELETE RESTRICT,
    Datum DATE,
    OdradeniSati FLOAT
);

insert into worklogentry (zaposlenikid, datum, odradenisati) 
values 
(1, '31-01-2023'::DATE, 8),
(2, '31-01-2023'::DATE, 6);


create table obracun(
    IDObracun SERIAL PRIMARY KEY,
    ZaposlenikID INT REFERENCES zaposlenik(ZaposlenikID) ON UPDATE CASCADE ON DELETE RESTRICT,
    UkupnoOdradeniSati FLOAT,
    SatnicaZaposlenika FLOAT,
    IznosZaIsplatu FLOAT
);

insert into obracun (zaposlenikid, UkupnoOdradeniSati, SatnicaZaposlenika, IznosZaIsplatu)
values
(1, 60, 35, 60*35);