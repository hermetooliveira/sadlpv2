CREATE DATABASE IF NOT EXISTS
    sadlpv;
USE sadlpv;

CREATE TABLE IF NOT EXISTS veiculos (
    id INT(11) AUTO_INCREMENT,
    proprietario VARCHAR(255),
    placa VARCHAR(255),
    chassi VARCHAR(255),
    situacao VARCHAR(255),
    marca_modelo_cor VARCHAR(255),    
    PRIMARY KEY (id)
);

INSERT INTO veiculos VALUE(0,'Hermeto Oliveira', 'PNM9200', '9BWAA45UXGP046401', 'VEICULO REGULAR', 'VW/GOL COR PRATA');
INSERT INTO veiculos VALUE(0,'Jorge Luiz Farias', 'OSA0670', '9BWAA45U7FP057970', 'CNH SUSPENSA', 'VW/GOL COR PRETA');
INSERT INTO veiculos VALUE(0,'Maria Gorette', 'POM1886', '8AP17164LD3036941', 'ROUBO/FURTO!', 'HYUNDAI/HB20 COR PRETA');
