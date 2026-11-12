SIGNOS = [
    ("Áries", (3, 21), (4, 20)), ("Touro", (4, 21), (5, 20)),
    ("Gêmeos", (5, 21), (6, 20)), ("Câncer", (6, 21), (7, 22)),
    ("Leão", (7, 23), (8, 22)), ("Virgem", (8, 23), (9, 22)),
    ("Libra", (9, 23), (10, 22)), ("Escorpião", (10, 23), (11, 21)),
    ("Sagitário", (11, 22), (12, 21)), ("Capricórnio", (12, 22), (1, 19)),
    ("Aquário", (1, 20), (2, 18)), ("Peixes", (2, 19), (3, 20)),
]

INFO_SIGNOS = {
    "Áries": {
        "palavras": "Corajoso, competitivo, impulsivo, líder, energético, pioneiro.",
        "texto": "Regido por Marte, é o primeiro signo do zodíaco. Possui uma energia inesgotável e um forte instinto de liderança. Não gosta de ficar parado e adora um desafio.",
        "curiosidade": "Na mitologia grega, representa o carneiro com o Velocino de Ouro. É o signo do fogo que inicia a roda do zodíaco."
    },
    "Touro": {
        "palavras": "Paciente, teimoso, leal, sensual, persistente, prático.",
        "texto": "Regido por Vênus, busca estabilidade, segurança e prazer nas coisas simples da vida. É extremamente confiável, mas pode ser inflexível quando contrariado.",
        "curiosidade": "Na mitologia, é o touro branco que Zeus se transformou para sequestrar Europa. Ama tudo o que é belo e material."
    },
    "Gêmeos": {
        "palavras": "Comunicativo, curioso, inteligente, adaptável, versátil.",
        "texto": "Regido por Mercúrio, é o signo da comunicação e das ideias. Tem uma mente brilhante e rápida, mas pode sofrer com a dualidade e a inconstância.",
        "curiosidade": "Representa os irmãos Castor e Pollux da mitologia. É conhecido como o signo dos 'dois lados' e da eterna juventude."
    },
    "Câncer": {
        "palavras": "Sensível, protetor, intuitivo, nostálgico, acolhedor.",
        "texto": "Regido pela Lua, tem uma conexão profunda com as emoções, o lar e a família. É superprotetor com quem ama e possui uma intuição afiadíssima.",
        "curiosidade": "O caranguejo tem uma carapaça dura por fora, mas é mole por dentro, simbolizando perfeitamente a defesa emocional deste signo."
    },
    "Leão": {
        "palavras": "Carismático, generoso, ambicioso, dramático, leal, criativo.",
        "texto": "Regido pelo Sol, é o centro das atenções. Tem uma vibe magnética, ama o luxo e a arte, e lidera com o coração. Sua maior necessidade é ser reconhecido.",
        "curiosidade": "O Leão da Nemeia, morto por Hércules, é seu símbolo. É o signo do fogo que representa a realeza e a força criativa."
    },
    "Virgem": {
        "palavras": "Analítico, perfeccionista, detalhista, prestativo, modesto.",
        "texto": "Regido por Mercúrio, tem um olhar clínico para o mundo. É o solucionador de problemas nato, sempre disposto a ajudar e a melhorar as coisas.",
        "curiosidade": "A deusa Astreia, da justiça, é sua regente mítica. Dizem que Virgem é o signo que melhor entende como o mundo funciona na prática."
    },
    "Libra": {
        "palavras": "Diplomático, sociável, elegante, indeciso, pacificador, justo.",
        "texto": "Regido por Vênus, busca a harmonia e o equilíbrio em todas as áreas. Tem um forte senso de estética e justiça, e odeia conflitos ou ambientes pesados.",
        "curiosidade": "A balança representa a pesagem das almas no julgamento de Osíris no Egito antigo. Libra é o único signo representado por um objeto."
    },
    "Escorpião": {
        "palavras": "Intenso, estrategista, leal, misterioso, transformador, corajoso.",
        "texto": "Regido por Marte e Plutão, nada é superficial para ele. Tem um poder de regeneração impressionante e uma lealdade feroz. Sabe guardar segredos como ninguém.",
        "curiosidade": "Ligado à figura do escorpião que matou Órion na mitologia. É o signo que rege a morte, o renascimento e as transformações profundas."
    },
    "Sagitário": {
        "palavras": "Otimista, aventureiro, filosófico, direto, livre, expansivo.",
        "texto": "Regido por Júpiter, é o viajante do zodíaco. Ama a liberdade, a filosofia e o conhecimento. Tem uma sinceridade que pode ser brutal, mas é movido por um otimismo contagiante.",
        "curiosidade": "O centauro Quíron, o grande sábio e curandeiro da mitologia, é seu símbolo. Está sempre mirando longe, com sua flecha apontada para o futuro."
    },
    "Capricórnio": {
        "palavras": "Disciplinado, ambicioso, responsável, prático, estratégico.",
        "texto": "Regido por Saturno, é o signo dos grandes construtores. Tem uma resiliência imensa e não tem medo do trabalho duro. Sabe esperar o tempo certo para colher seus frutos.",
        "curiosidade": "Representa o deus Pã, que se transformou em uma cabra-peixe para escapar do monstro Tifão. É o signo que rege as metas de longo prazo."
    },
    "Aquário": {
        "palavras": "Inovador, humanitário, rebelde, intelectual, original, visionário.",
        "texto": "Regido por Saturno e Urano, é o signo do futuro. Não segue padrões, pensa fora da caixa e se preocupa com o coletivo. Valoriza a amizade e a liberdade acima de tudo.",
        "curiosidade": "O aguadeiro da mitologia é Ganimedes, o copeiro dos deuses. Aquário rege a tecnologia, as causas sociais e as mudanças revolucionárias."
    },
    "Peixes": {
        "palavras": "Empático, intuitivo, artístico, sensível, sonhador, espiritualizado.",
        "texto": "Regido por Netuno, é o signo da dissolução dos limites. Tem uma conexão profunda com o mundo espiritual e as artes. Sente as emoções dos outros como se fossem suas.",
        "curiosidade": "Representa Afrodite e Eros, que se transformaram em peixes para escapar do monstro Tifão. É o último signo do zodíaco, simbolizando a fusão com o universo."
    },
}

def identificar_signo(dia, mes):
    for nome, (md, dd), (mm, dm) in SIGNOS:
        if nome == "Capricórnio":
            if (mes == md and dia >= dd) or (mes == mm and dia <= dm): return nome
        else:
            if (mes == md and dia >= dd) or (mes == mm and dia <= dm): return nome
    return "Desconhecido"