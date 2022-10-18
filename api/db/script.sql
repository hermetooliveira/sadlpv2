CREATE DATABASE IF NOT EXISTS
    sadlpv;
USE sadlpv;

CREATE TABLE IF NOT EXISTS veiculos (
    id INT(11) AUTO_INCREMENT,
    proprietario VARCHAR(255),
    placa VARCHAR(255),
    chassi VARCHAR(255),
    situacao VARCHAR(255),    
    PRIMARY KEY (id)
);

INSERT INTO veiculos VALUE(0,'Hermeto Oliveira', 'PNM9200', '123456789', 'VEICULO REGULAR');
INSERT INTO veiculos VALUE(0,'Jorge Luiz Farias', 'OSA0670', '101112131', 'CNH SUSPENSA');
INSERT INTO veiculos VALUE(0,'Adriana Costa Oliveira', 'OHY8327', '141516171', 'ROUBO/FURTO!');
