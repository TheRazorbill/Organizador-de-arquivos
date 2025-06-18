import os
import shutil
PASTA_ORIGEM_LIVROS = 'C:\\Users\\User\\Documents\\Arquivos DEV\\PASTA_ORIGEM_LIVROS'
CATEGORIAS_E_LIVROS = {
    "Algoritmos e Estruturas de Dados": [
        "Algoritmos - Teoria e Prática",
        "But How Do it Know",
        "Entendendo Algoritmos",
        "Expressões Regulares - uma abordagem divertida",
        "Introdução a data science"
    ],
    "Arquitetura de Software": [
        "Arquitetura Limpa",
        "Big Data - Técnicas e tecnologias",
        "Business Intelligence - Implementar do jeito certo",
        "Introdução à arquitetura de design de software",
        "Mergulho nos Padrões de Projeto",
        "Oauth 2.0 Proteja Suas Aplicações",
        "Princípios de Design e Padrões de Projeto",
        "Refatoração - Aperfeiçoando o Design de Códigos Existentes",
        "SOA Aplicado",
        "The Software Craftsman - Professionalism, Pragmatism, Pride",
        "Trabalho Eficaz com Código Legado"
    ],
    "Carreira e Habilidades": [
        "14 Hábitos de Desenvolvedores Altamente Produtivos",
        "A jornada do empreendedor",
        "A Startup Enxuta",
        "ABAP - O guia de Sobrevivência",
        "Apprenticeship Patterns",
        "Começando com o Linux",
        "Como mentir com estatística",
        "Como ser um Programador Melhor",
        "Direto ao Ponto - Criando produtos",
        "Fragmentos de um programador",
        "Gestão de produtos - Como aumentar as chances",
        "Guia da Startup",
        "Guia do Mestre Programador",
        "Learning 3.0",
        "O Programador Apaixonado",
        "O Programador Pragmático",
        "Por que Os Generalistas Vencem",
        "Range - Why Generalists Triumph",
        "Secrets of a Buccaneer-Scholar",
        "SEO Prático",
        "Soft Skills - The Software Developer's Life Manual",
        "The Mythical Man-Month",
        "The Passionate Programmer - Creating a Remarkable Career",
        "ThoughtWorks Antologia Brasil"
    ],
    "Desenvolvimento Ágil": [
        "Actionable Agile Metrics For Predictability",
        "Agile Estimating and Planning",
        "Agile Project Management with Scrum",
        "Agile - Desenvolvimento de Software com Entregas Frequentes",
        "BDD in Action",
        "Código limpo - Habilidades práticas do Agile Software",
        "Crystal Clear - A Human-Powered Methodology",
        "Desenvolvimento de Software com Scrum - Aplicando Métodos Ágeis",
        "eXtreme Programming - Práticas para o dia a dia",
        "Métricas ágeis - Obtenha melhores resultados",
        "Scrum - Gestão ágil para projetos",
        "Scrum 360",
        "Test-Driven Development - Teste e Design no Mundo Real",
        "Testes Automatizados de Software - Um Guia Prático"
    ],
    "DevOps": [
        "Amazon AWS - Descomplicando",
        "Aplicações web real time com Node-js",
        "Azure - Coloque suas plataformas",
        "Caixa de Ferramentas DevOps",
        "Canivete suiço do desenvolvedor Node",
        "Comunicação de Dados e Redes de Computadores",
        "Construindo API REST com Node JS",
        "Containers com Docker",
        "Controlando Versões com Git e GitHub",
        "DevOps na Prática",
        "Entrega contínua em Android",
        "Entrega Contínua - Como Entregar Software",
        "Guia prático do servidor Linux",
        "Jenkins - Automatize Tudo",
        "Kubernetes - Tudo sobre orquestração",
        "MongoDB - Construa Novas Aplicações",
        "NoSQL - Como armazenar os dados",
        "REST - Construa API's inteligentes"
    ],
    "Empresa e Cultura Organizacional": [
        "Agile Retrospectives - Making Good Teams Great",
        "A arte de dar feedback (Um guia acima da média)",
        "Coaching Agile Teams",
        "Como Melhorar o Desempenho da Sua Equipe",
        "LEAN ENTERPRISE - Como empresas de alta performance",
        "More Agile Testing - Learning Journeys",
        "Sprint - Autor (Jake Knapp)",
        "This is Lean - Resolving the Efficiency Paradox"
    ],
    "Entrevista e Preparação para Programação": [
        "Cracking the Coding Interview",
        "Front End Interview Handbook",
        "Guia prático de TypeScript",
        "Primeiros passos com Node.js",
        "TDD - Desenvolvimento Guiado por Testes",
        "Tech Interview Handbook"
    ],
    "Liderança e Gestão de Equipe": [
        "A Arte da Gestão - Um Guia Prático",
        "A Regra é Não Ter Regras - A Netflix",
        "O Ego É Seu Inimigo",
        "Managing For Happiness"
    ],
    "Metodologias Ágeis Avançadas": [
        "Clean Agile - Back to Basics",
        "Extreme Programming Explained - Embrace Change",
        "Implementando o Desenvolvimento Lean de Software",
        "Real-World Kanban",
        "Scaling Done Right",
        "The Cambridge Handbook of the Learning Sciences"
    ],
    "Padrões e Design de Software": [
        "A Web Mobile - Programe para um Mundo",
        "Clean Coder, The - A Code of Conduct",
        "CSS Eficiente - Técnicas e ferramentas",
        "Domain Driven Design Rapido",
        "Domain-Driven Design Referência",
        "Google Android - crie aplicações",
        "HTML5 e CSS3 - domine a web do futuro",
        "Padrões de Projetos - Soluções Reutilizáveis",
        "Progressive web apps - Construa aplicações",
        "UX e Usabilidade Aplicados em Mobile e Web",
        "Web Design Responsivo - Páginas adaptáveis"
    ]
}
PASTA_NAO_CATEGORIZADOS = "Nao Categorizados"
if not os.path.exists(PASTA_ORIGEM_LIVROS):
    print(f"Erro: A pasta de origem '{PASTA_ORIGEM_LIVROS}' não foi encontrada.")
    exit()
print(f"Iniciando a organização dos livros na pasta: {PASTA_ORIGEM_LIVROS}\n")
for categoria_nome in CATEGORIAS_E_LIVROS.keys():
    caminho_completo_pasta = os.path.join(PASTA_ORIGEM_LIVROS, categoria_nome)
    if not os.path.exists(caminho_completo_pasta):
        os.makedirs(caminho_completo_pasta)
        print(f"Pasta '{categoria_nome}' criada com sucesso.")
    else:
        print(f"Pasta '{categoria_nome}' já existe.")
caminho_nao_categorizados = os.path.join(PASTA_ORIGEM_LIVROS, PASTA_NAO_CATEGORIZADOS)
if not os.path.exists(caminho_nao_categorizados):
    os.makedirs(caminho_nao_categorizados)
    print(f"Pasta '{PASTA_NAO_CATEGORIZADOS}' criada para livros não categorizados.")
else:
    print(f"Pasta '{PASTA_NAO_CATEGORIZADOS}' já existe.")
print("\n--- Movendo arquivos de livros ---")
arquivos_nao_movidos = []
for nome_arquivo in os.listdir(PASTA_ORIGEM_LIVROS):
    caminho_arquivo_origem = os.path.join(PASTA_ORIGEM_LIVROS, nome_arquivo)
    if os.path.isdir(caminho_arquivo_origem) or nome_arquivo.startswith('.'):
        continue
    movido = False
    for categoria_nome, livros_keywords in CATEGORIAS_E_LIVROS.items():
        for keyword_livro in livros_keywords:

            if keyword_livro.lower() in nome_arquivo.lower():
                pasta_destino = categoria_nome
                caminho_destino_arquivo = os.path.join(PASTA_ORIGEM_LIVROS, pasta_destino, nome_arquivo)
                
                try:
                    shutil.move(caminho_arquivo_origem, caminho_destino_arquivo)
                    print(f"Movido: '{nome_arquivo}' para '{pasta_destino}'")
                    movido = True
                    break 
                except Exception as e:
                    print(f"Erro ao mover '{nome_arquivo}' para '{pasta_destino}': {e}")
                    arquivos_nao_movidos.append(nome_arquivo)
                    movido = True
                    break
        if movido:
            break
    if not movido:
        caminho_destino_nao_categorizados = os.path.join(PASTA_ORIGEM_LIVROS, PASTA_NAO_CATEGORIZADOS, nome_arquivo)
        try:
            shutil.move(caminho_arquivo_origem, caminho_destino_nao_categorizados)
            print(f"Movido: '{nome_arquivo}' para '{PASTA_NAO_CATEGORIZADOS}' (não categorizado)")
        except Exception as e:
            print(f"Erro ao mover '{nome_arquivo}' para '{PASTA_NAO_CATEGORIZADOS}': {e}")
            arquivos_nao_movidos.append(nome_arquivo)
print("\n--- Organização Concluída ---")
if arquivos_nao_movidos:
    print("\nOs seguintes arquivos NÃO foram movidos devido a erros ou já existirem no destino:")
    for arq in arquivos_nao_movidos:
        print(f"- {arq}")