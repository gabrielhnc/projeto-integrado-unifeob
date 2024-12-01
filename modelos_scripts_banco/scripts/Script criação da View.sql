CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `vw_completa` AS
    SELECT 
        `u`.`idusuario` AS `UsuarioID`,
        `u`.`nome` AS `UsuarioNome`,
        `u`.`email` AS `UsuarioEmail`,
        `u`.`telefone` AS `UsuarioTelefone`,
        `u`.`dataCadastro` AS `UsuarioDataCadastro`,
        `tu`.`tipo` AS `TipoUsuario`,
        `c`.`nome` AS `ColetorNome`,
        `c`.`cnpjCpf` AS `ColetorCnpjCpf`,
        `c`.`telefone` AS `ColetorTelefone`,
        `c`.`endereco` AS `ColetorEndereco`,
        `cid_c`.`nome` AS `ColetorCidade`,
        `est_c`.`nome` AS `ColetorEstado`,
        `a`.`idagendamento` AS `AgendamentoID`,
        `a`.`dataAgendamento` AS `AgendamentoData`,
        `a`.`hora` AS `AgendamentoHora`,
        `a`.`statusAgendamento` AS `AgendamentoStatus`,
        `m`.`nome` AS `MaterialNome`,
        `m`.`descricao` AS `MaterialDescricao`,
        `cat`.`categoria` AS `CategoriaMaterial`,
        `dep`.`nome` AS `DepositoNome`,
        `dep`.`endereco` AS `DepositoEndereco`,
        `dep`.`cep` AS `DepositoCEP`,
        `cid_d`.`nome` AS `DepositoCidade`,
        `est_d`.`nome` AS `DepositoEstado`,
        `dep`.`telefone` AS `DepositoTelefone`,
        `dep`.`capacidadeMaxima` AS `DepositoCapacidadeMaxima`,
        `dep`.`dataCadastro` AS `DepositoDataCadastro`,
        `e`.`identrada` AS `EntradaID`,
        `e`.`dataEntrada` AS `EntradaData`,
        `e`.`quantidade` AS `EntradaQuantidade`,
        `s`.`idsaida` AS `SaidaID`,
        `s`.`dataSaida` AS `SaidaData`,
        `s`.`quantidade` AS `SaidaQuantidade`,
        rk.posicao AS UsuarioPosicaoRanking,
        rk.quantidade_total AS UsuarioQuantidadeTotal,
        rk.ultima_entrada AS UsuarioUltimaEntrada
    FROM
        ((((((((((((`usuario` `u`
        JOIN `tipousuario` `tu` ON ((`u`.`tipoUsuario_idtipoUsuario` = `tu`.`idtipoUsuario`)))
        LEFT JOIN `entrada` `e` ON ((`u`.`idusuario` = `e`.`usuario_idusuario`)))
        LEFT JOIN `material` `m` ON ((`e`.`material_idmaterial` = `m`.`idmaterial`)))
        LEFT JOIN `categoria` `cat` ON ((`m`.`categoria_idcategoria` = `cat`.`idcategoria`)))
        LEFT JOIN `deposito` `dep` ON ((`e`.`deposito_iddeposito` = `dep`.`iddeposito`)))
        LEFT JOIN `cidade` `cid_d` ON ((`dep`.`cidade_idcidade` = `cid_d`.`idcidade`)))
        LEFT JOIN `estado` `est_d` ON ((`cid_d`.`estado_idestado` = `est_d`.`idestado`)))
        LEFT JOIN `saida` `s` ON ((`s`.`coletor_idcoletor` = `e`.`usuario_idusuario`)))
        LEFT JOIN `coletor` `c` ON ((`s`.`coletor_idcoletor` = `c`.`idcoletor`)))
        LEFT JOIN `cidade` `cid_c` ON ((`c`.`cidade_idcidade` = `cid_c`.`idcidade`)))
        LEFT JOIN `estado` `est_c` ON ((`cid_c`.`estado_idestado` = `est_c`.`idestado`)))
        LEFT JOIN `agendamento` `a` ON ((`a`.`coletor_idcoletor` = `c`.`idcoletor`)))
        LEFT JOIN (
            SELECT 
                RANK() OVER (ORDER BY SUM(e.quantidade) DESC) AS posicao,
                u.idusuario AS usuario_id,
                SUM(e.quantidade) AS quantidade_total,
                MAX(e.dataEntrada) AS ultima_entrada
            FROM 
                entrada e
            INNER JOIN usuario u ON e.usuario_idusuario = u.idusuario
            GROUP BY 
                u.idusuario
        ) rk ON u.idusuario = rk.usuario_id;
