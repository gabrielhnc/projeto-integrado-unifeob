## TIPO USUÁRIO

USE sboreciclasv;

INSERT INTO tipousuario (tipo) VALUES
('Cliente'),
('Funcionário'),
('Gerente'),
('Administrador'),
('Caixa'),
('Supervisor de Setor');


## USUÁRIO

INSERT INTO usuario (nome, email, telefone, dataCadastro, tipoUsuario_idtipoUsuario) VALUES
('Carlos Silva', 'carlos.silva@email.com', '11987654321', '2022-01-15', 1),
('Maria Oliveira', 'maria.oliveira@email.com', '11987654322', '2022-02-22', 2),
('João Souza', 'joao.souza@email.com', '11987654323', '2022-03-10', 3),
('Ana Costa', 'ana.costa@email.com', '11987654324', '2022-04-08', 4),
('Paulo Ferreira', 'paulo.ferreira@email.com', '11987654325', '2022-05-20', 5),
('Cláudia Lima', 'claudia.lima@email.com', '11987654326', '2022-06-01', 6),
('Ricardo Alves', 'ricardo.alves@email.com', '11987654327', '2022-07-11', 1),
('Fernanda Martins', 'fernanda.martins@email.com', '11987654328', '2022-08-25', 2),
('Juliana Ribeiro', 'juliana.ribeiro@email.com', '11987654329', '2022-09-30', 3),
('Felipe Pinto', 'felipe.pinto@email.com', '11987654330', '2022-10-14', 4),
('Camila Barbosa', 'camila.barbosa@email.com', '11987654331', '2022-11-17', 5),
('Thiago Santos', 'thiago.santos@email.com', '11987654332', '2022-12-01', 6),
('Gabriel Rocha', 'gabriel.rocha@email.com', '11987654333', '2023-01-05', 1),
('Luciana Dias', 'luciana.dias@email.com', '11987654334', '2023-02-12', 2),
('Rodrigo Melo', 'rodrigo.melo@email.com', '11987654335', '2023-03-18', 3),
('Patrícia Cunha', 'patricia.cunha@email.com', '11987654336', '2023-04-24', 4),
('Renato Campos', 'renato.campos@email.com', '11987654337', '2023-05-10', 5),
('Débora Nunes', 'debora.nunes@email.com', '11987654338', '2023-06-27', 6),
('Sérgio Batista', 'sergio.batista@email.com', '11987654339', '2023-07-11', 1),
('Isabela Cardoso', 'isabela.cardoso@email.com', '11987654340', '2023-08-02', 2),
('Vitor Carvalho', 'vitor.carvalho@email.com', '11987654341', '2023-09-19', 3),
('Bianca Almeida', 'bianca.almeida@email.com', '11987654342', '2023-10-04', 4),
('André Matos', 'andre.matos@email.com', '11987654343', '2023-11-15', 5),
('Larissa Moura', 'larissa.moura@email.com', '11987654344', '2023-12-31', 6);


## CATEGORIA

INSERT INTO categoria (categoria) VALUES
('Papel'),
('Plástico'),
('Metal'),
('Vidro'),
('Tetra Pak'),
('Bateria');


## MATERIAL

INSERT INTO material (nome, descricao, categoria_idcategoria)
VALUES
('Papelão', 'Material de papel grosso usado em embalagens', 1),
('Garrafa PET', 'Garrafa de plástico transparente para bebidas', 2),
('Lata de Alumínio', 'Lata de bebida feita de alumínio', 3),
('Vidro Transparente', 'Vidro de garrafa sem cor', 4),
('Caixa Tetra Pak', 'Embalagem cartonada usada para sucos e leite', 5),
('Pilha AA', 'Bateria cilíndrica usada em pequenos aparelhos', 6),
('Papel Branco', 'Papel usado para impressão', 1),
('Saco Plástico', 'Saco utilizado para embalar produtos', 2),
('Lata de Aço', 'Lata utilizada para alimentos enlatados', 3),
('Vidro Colorido', 'Vidro de garrafa com cor', 4),
('Papelão Ondulado', 'Papelão com ondulações para maior resistência', 1),
('Embalagem de Plástico', 'Embalagem utilizada para alimentos', 2),
('Lata de Tinta', 'Lata usada para armazenamento de tinta', 3),
('Garrafão de Vidro', 'Garrafão utilizado para armazenar líquidos', 4),
('Caixa de Leite Tetra Pak', 'Embalagem para leite feita de Tetra Pak', 5),
('Bateria de Lítio', 'Bateria recarregável usada em dispositivos eletrônicos', 6),
('Papel Jornal', 'Papel utilizado para impressão de jornais', 1),
('Plástico Filme', 'Plástico fino utilizado para embalagens', 2),
('Fio de Cobre', 'Material utilizado para fiação elétrica', 3),
('Caco de Vidro', 'Pedaços de vidro quebrado', 4);


## ESTADO

INSERT INTO estado (idestado, nome) VALUES
('AC', 'Acre'),
('AL', 'Alagoas'),
('AP', 'Amapá'),
('AM', 'Amazonas'),
('BA', 'Bahia'),
('CE', 'Ceará'),
('DF', 'Distrito Federal'),
('ES', 'Espírito Santo'),
('GO', 'Goiás'),
('MA', 'Maranhão'),
('MT', 'Mato Grosso'),
('MS', 'Mato Grosso do Sul'),
('MG', 'Minas Gerais'),
('PA', 'Pará'),
('PB', 'Paraíba'),
('PR', 'Paraná'),
('PE', 'Pernambuco'),
('PI', 'Piauí'),
('RJ', 'Rio de Janeiro'),
('RN', 'Rio Grande do Norte'),
('RS', 'Rio Grande do Sul'),
('RO', 'Rondônia'),
('RR', 'Roraima'),
('SC', 'Santa Catarina'),
('SP', 'São Paulo'),
('SE', 'Sergipe'),
('TO', 'Tocantins');


## CIDADE

INSERT INTO cidade (nome, estado_idestado) VALUES
('Americana', 'SP'),
('Campinas', 'SP'),
('Santa Bárbara dOeste', 'SP'),
('Santo André', 'SP'),
('Valinhos', 'SP'),
('Vinhedo', 'SP'),
('Indaiatuba', 'SP'),
('Itatiba', 'SP'),
('Jundiaí', 'SP'),
('Nova Odessa', 'SP'),
('Paulínia', 'SP'),
('São João da Boa Vista', 'SP'),
('Sorocaba', 'SP'),
('Sumaré', 'SP'),
('Tatuí', 'SP'),
('Vinhedo', 'SP');


## COLETOR

INSERT INTO coletor (nome, cnpjCpf, telefone, endereco, cidade_idcidade, dataCadastro) 
VALUES
('ACME Indústria de Comércio de Lixo', '59.764.555/0001-52', '11987657294', 'Rua A, 123', 1, '2024-01-15'),
('Reciclável Soluções Ambientais', '12.345.678/0001-98', '11987654321', 'Rua B, 456', 2, '2024-02-10'),
('Green Future Coleta e Reciclagem', '34.567.890/0001-23', '11987651234', 'Avenida C, 789', 3, '2024-03-05'),
('Lixo Limpo Ltda.', '98.765.432/0001-11', '11987652345', 'Praça D, 147', 4, '2024-04-20'),
('Eco Coleta Ambiental', '87.654.321/0001-99', '11987653456', 'Rua E, 258', 5, '2024-05-25'),
('ReciclaBrasil', '56.789.012/0001-76', '11987654567', 'Avenida F, 369', 6, '2024-06-30'),
('Limpando o Futuro', '45.678.901/0001-55', '11987655678', 'Rua G, 852', 7, '2024-07-15'),
('Indústria Verde Coleta', '23.456.789/0001-44', '11987656789', 'Praça H, 963', 8, '2024-08-10'),
('Reciclagem Total', '67.890.123/0001-22', '11987657890', 'Rua I, 741', 9, '2024-09-05'),
('Coleta Ecológica', '78.901.234/0001-33', '11987658901', 'Avenida J, 258', 10, '2024-10-01'),
('Resíduos Sustentáveis', '89.012.345/0001-11', '11987659012', 'Rua K, 369', 11, '2024-11-20'),
('Indústria de Reciclagem Ecocycle', '90.123.456/0001-88', '11987660123', 'Praça L, 852', 12, '2024-12-15'),
('Lixo Verde Coleta', '21.234.567/0001-77', '11987661234', 'Rua M, 963', 13, '2024-01-05'),
('Reciclar é Viver', '32.345.678/0001-66', '11987662345', 'Avenida N, 147', 14, '2024-02-10'),
('Indústria de Coleta Ecológica', '43.456.789/0001-55', '11987663456', 'Rua O, 258', 15, '2024-03-25');


## DEPÓSITO

INSERT INTO deposito (iddeposito, nome, endereco, cep, cidade_idcidade, telefone, capacidadeMaxima, dataCadastro, horaAbertura, horaFechamento) VALUES
(1, 'Mercado São Rafael', 'R. Monsenhor João Ramalho, 777 - Jardim Nova Republica', '13875-249', 12, '1936313528', 100, '2024-09-25', '07:00:00', '21:00:00');


## AGENDAMENTO

INSERT INTO agendamento (dataAgendamento, hora, statusAgendamento, coletor_idcoletor) VALUES
('2024-10-18', '08:30:00', 'Pendente', 1),
('2024-10-19', '14:00:00', 'Concluído', 2),
('2024-10-20', '09:15:00', 'Cancelado', 3),
('2024-10-21', '16:45:00', 'Pendente', 4),
('2024-10-22', '10:30:00', 'Concluído', 5),
('2024-10-23', '11:00:00', 'Pendente', 6),
('2024-10-24', '13:20:00', 'Concluído', 7),
('2024-10-25', '15:00:00', 'Pendente', 8),
('2024-10-26', '12:45:00', 'Cancelado', 9),
('2024-10-27', '07:30:00', 'Concluído', 10),
('2024-10-28', '08:00:00', 'Pendente', 11),
('2024-10-29', '14:30:00', 'Concluído', 12),
('2024-10-30', '09:00:00', 'Cancelado', 13),
('2024-10-31', '16:00:00', 'Pendente', 14),
('2024-11-01', '10:15:00', 'Concluído', 15);


## ENTRADA

INSERT INTO entrada (usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade) VALUES
(1, 1, 1, '2024-01-01', 10.00),
(2, 1, 2, '2024-01-02', 15.00),
(3, 1, 3, '2024-01-03', 25.00),
(4, 1, 4, '2024-01-04', 30.00),
(5, 1, 5, '2024-01-05', 20.00),
(6, 1, 6, '2024-01-06', 18.00),
(7, 1, 7, '2024-01-07', 22.00),
(8, 1, 8, '2024-01-08', 24.00),
(9, 1, 9, '2024-01-09', 12.00),
(10, 1, 10, '2024-01-10', 28.00),
(11, 1, 11, '2024-01-11', 19.00),
(12, 1, 12, '2024-01-12', 23.00),
(13, 1, 13, '2024-01-13', 17.00),
(14, 1, 14, '2024-01-14', 21.00),
(15, 1, 15, '2024-01-15', 13.00),
(16, 1, 16, '2024-01-16', 26.00),
(17, 1, 17, '2024-01-17', 14.00),
(18, 1, 18, '2024-01-18', 29.00),
(19, 1, 19, '2024-01-19', 16.00),
(20, 1, 20, '2024-01-20', 27.00),
(21, 1, 3, '2024-01-21', 30.00),
(22, 1, 5, '2024-01-22', 25.00),
(23, 1, 8, '2024-01-23', 24.00),
(24, 1, 14, '2024-01-24', 22.00);


## SAIDA

INSERT INTO saida (deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade) VALUES
(1, 1, 1, '2024-01-01', 10.00),
(1, 2, 2, '2024-01-02', 15.00),
(1, 3, 3, '2024-01-03', 25.00),
(1, 4, 4, '2024-01-04', 30.00),
(1, 5, 5, '2024-01-05', 20.00),
(1, 6, 6, '2024-01-06', 18.00),
(1, 7, 7, '2024-01-07', 22.00),
(1, 8, 8, '2024-01-08', 24.00),
(1, 9, 9, '2024-01-09', 12.00),
(1, 10, 10, '2024-01-10', 28.00),
(1, 11, 11, '2024-01-11', 19.00),
(1, 12, 12, '2024-01-12', 23.00),
(1, 13, 13, '2024-01-13', 17.00),
(1, 14, 14, '2024-01-14', 21.00),
(1, 15, 15, '2024-01-15', 13.00),
(1, 10, 16, '2024-01-16', 26.00),
(1, 12, 17, '2024-01-17', 14.00),
(1, 7, 18, '2024-01-18', 29.00),
(1, 4, 19, '2024-01-19', 16.00),
(1, 3, 20, '2024-01-20', 27.00),
(1, 10, 3, '2024-01-21', 30.00),
(1, 11, 5, '2024-01-22', 25.00),
(1, 14, 8, '2024-01-23', 24.00),
(1, 2, 14, '2024-01-24', 22.00);
