def adapters(statement_comparison_function, response_selection_method):

    logic_adapters = [
                        {
                            "import_path": "chatterbot.logic.BestMatch",
                            "statement_comparison_function": statement_comparison_function,
                            "response_selection_method": response_selection_method,
                            'default_response': 'Olá, sou o Ocomon. Para que eu possa te ajudar, envie perguntas do tipo "Anunciar Oportunidade de Bolsa".',
                            'maximum_similarity_threshold': 0.85
                        },

                            {
                            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                            'input_text': 'ajuda',
                            'output_text': 'Tente outros canais de suporte ao usuário: ctic-atendimento@unifesspa.edu.br, (94) 2101 - 5945, Atendimento CTIC (Spark), Portal CTIC ou WIKI Unifesspa.'
                        },

                        {
                            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                            'input_text': 'saudacoes',
                             'output_text': 'Olá, sou o Ocomon, estou aqui para ajudar a solucionar alguns problemas relacionados a sistemas, serviços e suporte da unifesspa. Qual o problema deseja solucionar?'
                        },

                        {
                            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                            'input_text': 'tarde',
                            'output_text': 'Boa tarde!! Olá, sou o Ocomon, estou aqui para ajudar a solucionar alguns problemas relacionados a sistemas, serviços e suporte da unifesspa. Qual o problema deseja solucionar?'
                        },

                        {
                            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                            'input_text': 'manha',
                            'output_text': 'Bom dia!! Olá, sou o Ocomon, estou aqui para ajudar a solucionar alguns problemas relacionados a sistemas, serviços e suporte da unifesspa. Qual o problema deseja solucionar?'
                        },

                        {
                            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                            'input_text': 'noite',
                            'output_text': 'Boa noite!! Olá, sou o Ocomon, estou aqui para ajudar a solucionar alguns problemas relacionados a sistemas, serviços e suporte da unifesspa. Qual o problema deseja solucionar?'
                        }
                    ]
    return  logic_adapters