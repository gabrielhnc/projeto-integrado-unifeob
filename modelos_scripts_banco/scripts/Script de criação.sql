-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SBOReciclaSV
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SBOReciclaSV
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SBOReciclaSV` DEFAULT CHARACTER SET utf8 ;
USE `SBOReciclaSV` ;

-- -----------------------------------------------------
-- Table `SBOReciclaSV`.`tipoUsuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SBOReciclaSV`.`tipoUsuario` (
  `idtipoUsuario` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NULL,
  PRIMARY KEY (`idtipoUsuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SBOReciclaSV`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SBOReciclaSV`.`usuario` (
  `idusuario` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `email` VARCHAR(50) NULL,
  `telefone` VARCHAR(20) NULL,
  `dataCadastro` DATE NULL,
  `tipoUsuario_idtipoUsuario` INT NOT NULL,
  PRIMARY KEY (`idusuario`, `tipoUsuario_idtipoUsuario`),
  INDEX `fk_usuario_tipoUsuario1_idx` (`tipoUsuario_idtipoUsuario` ASC) VISIBLE,
  CONSTRAINT `fk_usuario_tipoUsuario1`
    FOREIGN KEY (`tipoUsuario_idtipoUsuario`)
    REFERENCES `SBOReciclaSV`.`tipoUsuario` (`idtipoUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SBOReciclaSV`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SBOReciclaSV`.`categoria` (
  `idcategoria` INT NOT NULL AUTO_INCREMENT,
  `categoria` VARCHAR(45) NULL,
  PRIMARY KEY (`idcategoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SBOReciclaSV`.`material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SBOReciclaSV`.`material` (
  `idmaterial` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(50) NULL,
  `descricao` VARCHAR(100) NULL,
  `categoria_idcategoria` INT NOT NULL,
  PRIMARY KEY (`idmaterial`, `categoria_idcategoria`),
  INDEX `fk_material_categoria1_idx` (`categoria_idcategoria` ASC) VISIBLE,
  CONSTRAINT `fk_material_categoria1`
    FOREIGN KEY (`categoria_idcategoria`)
    REFERENCES `SBOReciclaSV`.`categoria` (`idcategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SBOReciclaSV`.`estado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SBOReciclaSV`.`estado` (
  `idestado` VARCHAR(2) NOT NULL,
  `nome` VARCHAR(30) NULL,
  PRIMARY KEY (`idestado`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SBOReciclaSV`.`cidade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SBOReciclaSV`.`cidade` (
  `idcidade` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(50) NULL,
  `estado_idestado` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`idcidade`, `estado_idestado`),
  INDEX `fk_cidade_estado1_idx` (`estado_idestado` ASC) VISIBLE,
  CONSTRAINT `fk_cidade_estado1`
    FOREIGN KEY (`estado_idestado`)
    REFERENCES `SBOReciclaSV`.`estado` (`idestado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SBOReciclaSV`.`coletor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SBOReciclaSV`.`coletor` (
  `idcoletor` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `cnpjCpf` VARCHAR(20) NULL,
  `telefone` VARCHAR(20) NULL,
  `endereco` VARCHAR(100) NULL,
  `dataCadastro` DATE NULL,
  `cidade_idcidade` INT NOT NULL,
  PRIMARY KEY (`idcoletor`, `cidade_idcidade`),
  INDEX `fk_coletor_cidade1_idx` (`cidade_idcidade` ASC) VISIBLE,
  CONSTRAINT `fk_coletor_cidade1`
    FOREIGN KEY (`cidade_idcidade`)
    REFERENCES `SBOReciclaSV`.`cidade` (`idcidade`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SBOReciclaSV`.`agendamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SBOReciclaSV`.`agendamento` (
  `idagendamento` INT NOT NULL AUTO_INCREMENT,
  `dataAgendamento` DATE NULL,
  `statusAgendamento` VARCHAR(12) NULL,
  `hora` TIME NULL,
  `coletor_idcoletor` INT NOT NULL,
  PRIMARY KEY (`idagendamento`),
  INDEX `fk_agendamento_coletor1_idx` (`coletor_idcoletor` ASC) VISIBLE,
  CONSTRAINT `fk_agendamento_coletor1`
    FOREIGN KEY (`coletor_idcoletor`)
    REFERENCES `SBOReciclaSV`.`coletor` (`idcoletor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SBOReciclaSV`.`deposito`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SBOReciclaSV`.`deposito` (
  `iddeposito` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `endereco` VARCHAR(100) NULL,
  `cep` VARCHAR(10) NULL,
  `telefone` VARCHAR(20) NULL,
  `capacidadeMaxima` FLOAT NULL,
  `dataCadastro` DATE NULL,
  `horaAbertura` TIME NULL,
  `horaFechamento` TIME NULL,
  `cidade_idcidade` INT NOT NULL,
  PRIMARY KEY (`iddeposito`, `cidade_idcidade`),
  INDEX `fk_deposito_cidade1_idx` (`cidade_idcidade` ASC) VISIBLE,
  CONSTRAINT `fk_deposito_cidade1`
    FOREIGN KEY (`cidade_idcidade`)
    REFERENCES `SBOReciclaSV`.`cidade` (`idcidade`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SBOReciclaSV`.`saida`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SBOReciclaSV`.`saida` (
  `idsaida` INT NOT NULL AUTO_INCREMENT,
  `dataSaida` DATE NULL,
  `quantidade` FLOAT NULL,
  `material_idmaterial` INT NOT NULL,
  `coletor_idcoletor` INT NOT NULL,
  `deposito_iddeposito` INT NOT NULL,
  PRIMARY KEY (`idsaida`, `material_idmaterial`, `coletor_idcoletor`, `deposito_iddeposito`),
  INDEX `fk_saida_coletor1_idx` (`coletor_idcoletor` ASC) VISIBLE,
  INDEX `fk_saida_deposito1_idx` (`deposito_iddeposito` ASC) VISIBLE,
  INDEX `fk_saida_material1_idx` (`material_idmaterial` ASC) VISIBLE,
  CONSTRAINT `fk_saida_coletor1`
    FOREIGN KEY (`coletor_idcoletor`)
    REFERENCES `SBOReciclaSV`.`coletor` (`idcoletor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_saida_deposito1`
    FOREIGN KEY (`deposito_iddeposito`)
    REFERENCES `SBOReciclaSV`.`deposito` (`iddeposito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_saida_material1`
    FOREIGN KEY (`material_idmaterial`)
    REFERENCES `SBOReciclaSV`.`material` (`idmaterial`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SBOReciclaSV`.`entrada`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SBOReciclaSV`.`entrada` (
  `identrada` INT NOT NULL AUTO_INCREMENT,
  `dataEntrada` DATE NULL,
  `quantidade` FLOAT NULL,
  `material_idmaterial` INT NOT NULL,
  `deposito_iddeposito` INT NOT NULL,
  `usuario_idusuario` INT NOT NULL,
  PRIMARY KEY (`identrada`, `material_idmaterial`, `deposito_iddeposito`, `usuario_idusuario`),
  INDEX `fk_entrada_usuario1_idx` (`usuario_idusuario` ASC) VISIBLE,
  INDEX `fk_entrada_deposito1_idx` (`deposito_iddeposito` ASC) VISIBLE,
  INDEX `fk_entrada_material1_idx` (`material_idmaterial` ASC) VISIBLE,
  CONSTRAINT `fk_entrada_usuario1`
    FOREIGN KEY (`usuario_idusuario`)
    REFERENCES `SBOReciclaSV`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_entrada_deposito1`
    FOREIGN KEY (`deposito_iddeposito`)
    REFERENCES `SBOReciclaSV`.`deposito` (`iddeposito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_entrada_material1`
    FOREIGN KEY (`material_idmaterial`)
    REFERENCES `SBOReciclaSV`.`material` (`idmaterial`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
