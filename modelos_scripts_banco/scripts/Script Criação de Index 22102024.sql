# Para melhorar a performance das consultas foi criado indices em todas as tabelas nos principais campos de busca. 

CREATE INDEX idx_tipo ON `SBOReciclaSV`.`tipoUsuario` (`tipo`);

CREATE INDEX idx_nome ON `SBOReciclaSV`.`usuario` (`nome`);

CREATE INDEX idx_categoria ON `SBOReciclaSV`.`categoria` (`categoria`);

CREATE INDEX idx_nome ON `SBOReciclaSV`.`material` (`nome`);

CREATE INDEX idx_nome ON `SBOReciclaSV`.`estado` (`nome`);

CREATE INDEX idx_nome ON `SBOReciclaSV`.`cidade` (`nome`);

CREATE INDEX idx_nome ON `SBOReciclaSV`.`coletor` (`nome`);

CREATE INDEX idx_status ON `SBOReciclaSV`.`agendamento` (`status`);

CREATE INDEX idx_nome ON `SBOReciclaSV`.`deposito` (`nome`);

CREATE INDEX idx_dataSaida ON `SBOReciclaSV`.`saida` (`dataSaida`);

CREATE INDEX idx_dataEntrada ON `SBOReciclaSV`.`entrada` (`dataEntrada`);
