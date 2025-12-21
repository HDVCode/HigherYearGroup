from keyBranchNode import keyBranchNode
from infoBranchNode import infoBranchNode

def createCompanyTree():

    # -------- Root --------
    root = keyBranchNode("Ceo", b'aBD5a1lGQxIffPPbKCHPsGOzLhscCTnUydC2zOqLthA=')

    # COO / Chief of Staff (has access to most things)
    root.addChild(keyBranchNode("CooChiefOfStaff", b'lRXVcqO6ROvssToHMo7eBeNcVgitYrk4vD4uGsRzSx0='))

    # -------- HR branch --------
    root.addChild(keyBranchNode("HrHead", b'Nkc3BYWObpxp8OIw7rczeNDUBk5p32TH5JGjWr1TnGg='))
    root.getChildReferenceDFS("HrHead").addChild(
        keyBranchNode("HrManager", b'bj3NHA7TfJu2Z9-0WxC8oBirYGyZQeNzIO-zWc9zpwI=')
    )
    root.getChildReferenceDFS("HrManager").addChild(keyBranchNode("HrSpecialist1", b'003hgpWjT325hhdYJmP4Sdh2IlMBm4fZndy7dK6N2oE='))
    root.getChildReferenceDFS("HrManager").addChild(keyBranchNode("HrSpecialist2", b'V_BwxRHo7LbjiBom4BmO-MghBb2VlxJpQfm8TGnkloI='))
    root.getChildReferenceDFS("HrSpecialist1").addChild(keyBranchNode("HrIntern1", b'rrh8JWDDO3yWW8XutOjoi5DxiDim-_Qokj1IDfwyr5A='))
    root.getChildReferenceDFS("HrSpecialist2").addChild(keyBranchNode("HrIntern2", b'RVEhAM7UMvHPTzaRBUsBr4NoW-qEQJDU3AOOGQSPgXQ='))

    # -------- Tech branch --------
    root.addChild(keyBranchNode("LeadDev", b'wsOKyxju9sjgh4wHOIhUECi1TcdQPve90ZI3nmWE5h4='))

    root.getChildReferenceDFS("LeadDev").addChild(keyBranchNode("SeniorDev1", b'F0Jg6hY-ctTB50Cyp81mpOuaorBXgms6xnbeWWO6zRs='))
    root.getChildReferenceDFS("LeadDev").addChild(keyBranchNode("SeniorDev2", b'4LOj9ah-m0_rv0J7-a6uCOY5t1oAa5RqkiVyH-kt5RA='))

    root.getChildReferenceDFS("SeniorDev1").addChild(keyBranchNode("JuniorDev1", b'vXKGzn_h-XRRO93lBO3GCcfHguPyZ4lv9jLWtVq_WpI='))
    root.getChildReferenceDFS("SeniorDev1").addChild(keyBranchNode("JuniorDev2", b'MEbkkKcnreoEYI0UBnDr4fjRbr1XRByVsRFYIw3IzFQ='))

    root.getChildReferenceDFS("SeniorDev1").addChild(keyBranchNode("JuniorDev3", b'o7g_nCxY6yYD-muEgHnd9-xVbiJvX1xBUKi5wMCvfig='))
    root.getChildReferenceDFS("SeniorDev2").addChild(keyBranchNode("JuniorDev4", b'C5svxn37IGr0wjjBejw4JFsqRrmn4NbsRV0HzuTvvHE='))
    root.getChildReferenceDFS("SeniorDev2").addChild(keyBranchNode("JuniorDev5", b'vApVQH-Eh24GBkWPbPoMoWi3GiYzyNVOz7gczuJQq60='))

    # QA branch
    root.getChildReferenceDFS("LeadDev").addChild(keyBranchNode("QaLead", b'IiDYf3QzGTUpgimwGdMWvIvD6YZxB2juoMH0E4KwN90='))
    root.getChildReferenceDFS("QaLead").addChild(keyBranchNode("QaEngineer1", b'JCmrL5NuMIXKw5eht2AQOAi7TOpETkWpR-5kRlxg3UA='))
    root.getChildReferenceDFS("QaLead").addChild(keyBranchNode("QaEngineer2", b'8k8SD_YfopXNXsFPVO9MWZ6l8NeBAw3fTBfgqQRfWYQ='))
    root.getChildReferenceDFS("QaLead").addChild(keyBranchNode("QaIntern", b'0h9ds2ffLD2BgUQgkmtggzbXD80glL2r2lkKpS4dtYY='))

    # -------- Marketing branch --------
    root.addChild(keyBranchNode("MarketingHead", b'LfHBlbr6Y8anei3azC2GeKp2BxuUl9C0O66Jcg8Z_WQ='))
    root.getChildReferenceDFS("MarketingHead").addChild(keyBranchNode("MarketingSpecialist1", b'qKGle8bDWWRqzI7a6qW2JVA1Zex2tts0IwaLwydlw5c='))
    root.getChildReferenceDFS("MarketingHead").addChild(keyBranchNode("MarketingSpecialist2", b'YIgrCUFm0JZBOhTncIjC5aNOC32DK2rTGp95YTnCXws='))
    root.getChildReferenceDFS("MarketingHead").addChild(keyBranchNode("SocialMediaManager", b'3xZPXaedT3KRyKHppRjJC-kFJGVBbTMOBYMWgNJIY4A='))
    root.getChildReferenceDFS("SocialMediaManager").addChild(keyBranchNode("ContentCreator1", b'0ZwK6qnin5ePi8jvbg6KxWLzIQH-oL-nk3LAGCfoImk='))
    root.getChildReferenceDFS("SocialMediaManager").addChild(keyBranchNode("ContentCreator2", b'gwzQjfma35qkms4SEH1s4SwO7aEWBRixVmPpvs0qf_M='))

    # -------- Sales branch --------
    root.addChild(keyBranchNode("SalesHead", b'8w3J0oAFqGg4RPkLL6ZK8cMzGkKYiN43W6S_8DXTR5M='))
    root.getChildReferenceDFS("SalesHead").addChild(keyBranchNode("SalesManager1", b'plCN9swfagK63RYCrnfm5tn3Kb4VwE_ALWAI50jY9ok='))
    root.getChildReferenceDFS("SalesHead").addChild(keyBranchNode("SalesManager2", b'yQiIdWw7mecI6bYjPzuYtffEdYQV2WDurcbL1npK9vU='))
    root.getChildReferenceDFS("SalesManager1").addChild(keyBranchNode("SalesRep1", b'6NHNZXcyKO9A_e6MkJSW_0JK3K0uY2uPpTrDomzs9Cg='))
    root.getChildReferenceDFS("SalesManager1").addChild(keyBranchNode("SalesRep2", b'IMmP7--NkY3QoqGvEHJS3UcblL9YnY8kKN6SB2aeBYY='))
    root.getChildReferenceDFS("SalesManager2").addChild(keyBranchNode("SalesRep3", b'ylq6WNZ4gPn8lqcELC_At3zy4RkZJx4XLN2iRgqpmio='))

    # -------- Finance branch --------
    root.addChild(keyBranchNode("FinanceHead", b'ENZVgBHCLFpK6ijI1d6dQIAS15ukImxtOtDUyMgmo8A='))
    root.getChildReferenceDFS("FinanceHead").addChild(keyBranchNode("Accountant1", b'H7vOXWRh28mZaWuSAE9V1mdyPeKwSohunNmge4SMRt0='))
    root.getChildReferenceDFS("FinanceHead").addChild(keyBranchNode("Accountant2", b'cwAK6ySwSetAHUgEP6iWsE09q5yBWqsPQCaAj855rnQ='))

    # -------- Operations branch --------
    root.addChild(keyBranchNode("OperationsHead", b'7RTrxe-cuuQhrXvKyqrpCWShFuKzRwg8u9ztEBlx5RA='))

    return root


def initializeAllMessages():

    messagesData = {

        # CEO & COO
        "Ceo": b'gAAAAABpPSsiWpzqoM8hHP0Z4qNanlSgWtuv3Yfo10ktfXzj-quyLJQVqAGfbl0lxOYneYlR906frNtIIxXoqlsFYl-HxrJhmtv-XgWD-_MCzdDpgUHfIfbt7-taPrWrUDUt_LcvAHSKRhdhv8-KMKKyogORtYq_8w==',
        "CooChiefOfStaff": b'gAAAAABpPSsi0SWfNkaaOg0vf3a4-BlofmdJHpdjA5gbTgN7ZT0CJOQlx5ha_EC2oUwhpmruEB4P1TwxJjAGvXnQHSCLpa1pzs5RdV-RiCQR34zrWw2eg38=',

        # HR branch
        "HrHead": b'gAAAAABpPSsisyPSqfEhjK7EMskxE6RpiQoYiLySE--hj8m9Iba6akfywIRpfF-UkoMa-0zVe5v-w5h5bCT5R4l3ymhmUEaC5jyQTAShEDrAdiBB561qsjI=',
        "HrManager": b'gAAAAABpPSsiReqoikn8kb82Q0NNDYz5Ew_DuGBpZ9dHIKf3RTkdjonJJrUp-mZ9LimEhNdA-twyC5JQ_N6wEEVqJKsG9bolcQ==',
        "HrSpecialist1": b'gAAAAABpPSsiDVRJTZOd2qmggEQwWjomNpkUYBiBMpmA3GSlKfYGiihLobxYzESmiIX9guICrNDUpGHzSxaG8XPBQ6fTm5pFhD1SbMiDxsdKXt5FfUnSPExXCWfzEwnd4heL1aQSYG7l',
        "HrSpecialist2": b'gAAAAABpPSsi5OfH4AUsND--JKbD2ziz1uXJrlzVwWi-807ENbhpD03B-_kfVAfBo7ciwUQhWihgeSllqdH3hY2npa_Dj5kgWtcvMMkJBWy5sldLjaVr3d0=',
        "HrIntern1": b'gAAAAABpPSsieHTOm_tbsh7bEJ6W_3T4El1NKfnZchbEScSjVr4afJuO5y6Zjl4EXRo4U1qm18hYna9ISX3ALE-BlsYRKItJHlsGNa5_aIvRugHV7h1eP7fjUSh1ty4EcmYV2_ACR0Y7',
        "HrIntern2": b'gAAAAABpPSsiKMVqomTodhwQ3kQkuDxhG3gbOa07aPmP7J-hQic7ldLr0fkXJAgbXkZpCOQChhHu2q4DEXO-Gd1gcEf2MuZVHXXSF5rukToxeKwBnOCcaUY=',

        # Tech branch
        "LeadDev": b'gAAAAABpPSsiGgg6ET6zMChnw0ClEu47IOwl8zbrXRZRHaizehjaC9kXcgIDaSIZ5a0I3CeeTu93x6B2FmfQw_E9_RYCUCCcqw==',
        "SeniorDev1": b'gAAAAABpPSsiE6_M9gGRR0Qn_3Ba4l9i9_qitiluFgJhYbVeGWPc8jvuCLMwXsg9ZzQyEr1rar5YVl_VNk6Xb013b-brgtjGQQ==',
        "SeniorDev2": b'gAAAAABpPSsiVPr2jMjUG2ClKPZCr-EkjHXK2UdIsA2nsFOj-aNy0OAmOo4gWeNbydIGhTo9EKFrBnqXFnGKLI-z9Hxx3EvtuUWwZG4TXpRH2LgQNLI9jEw=',
        "JuniorDev1": b'gAAAAABpPSsic8ijefwctRgFkScUvlaqgWbv-4S9KW2YJ8l1g70m8s4eWjk0ioVfi0wdXEOPttcqdxGnlzDrbOwN6ORj8U9OLIsWcvUhduOLYgDynJqG3e8=',
        "JuniorDev2": b'gAAAAABpPSsi_Cl3eE4bR1DkHJIjb-OHxEi2IEZ4xasxQ8Nx9oQCCj9SsKmowbmwpXiRLMR67JuuuxyaCpwMNw9Y4Gncpp6vFA==',
        "JuniorDev3": b'gAAAAABpPSsiaHhNPUn8mFFQvd9FTSuMYm6yEiXXXaWyuPxVKNs4OYHHu4DV65uDO7r7WS36ffs6BTQsv5dJ5wtH6g5gkFZ_WK9hf2vt_SK4G51lhp98hpU=',
        "JuniorDev4": b'gAAAAABpPSsiSJoSm7YthR2sqa-wrpQwr6Ug_pdmeX3JwXgccdrDL_BZzIMt8xqBo14hV_78KeR_-MVqV9AfbwJ3vqpgV_6gU77Y5UvJkoXxz4j5F1LBH34=',
        "JuniorDev5": b'gAAAAABpPSsiuIU3E2CBoIJ0SMy1vieM_b9ljYy6bbzzl2iAKf_5YihQtoqlwARpBiQhwDSgwO34c4u6P7jgB7HsaUFj8y7Y6w==',

        # QA branch
        "QaLead": b'gAAAAABpPSsixJwSNXzxOvspxS9IRRYlrCo9dhNgHVn3ND2w-7wirj5zxQ6B4q-kLGweT1VKHElEqShXQfSXKCBngUqKTdC-6Qu6e6RHM4_4byUMDMaYqSg=',
        "QaEngineer1": b'gAAAAABpPSsi_KDfbW40uL0aU0g8nUz6dgqyRbF8v-P6LiXrhpVwdGdAFUILV3IFbXBGGauEShaeBfH5HVYlfIY4sUJ40i_Dki4oxUS7I3NuEF17tWR2e8o=',
        "QaEngineer2": b'gAAAAABpPSsig_YPCw1zaim01ZaEY2dp4knyhrQZMbrzkSQMCtswybuV5DHifUd6o1nUtCr1frn2JEdc5PKZ9Y_6tQADDwyDJz-efdHsTbfvNeT_RQrfspk=',
        "QaIntern": b'gAAAAABpPSsif_Jmoj22xHj-rB-TJdBq9lwvji_9c2QGgSMMuAggDSllqNbMBVjUKV25DmKRepBC6qG1gN7FYEaew8E7rBIeruW9396quoR989d4VnFld8M=',

        # Marketing branch
        "MarketingHead": b'gAAAAABpPSsiAtks-qq0ZOvvq61lByEVjnpDntBuCqTbGueYCeZfr4NmQ5scr84lyerVCyme-GAQZ9G4Wc69oQ4dtYicEOGuGA==',
        "MarketingSpecialist1": b'gAAAAABpPSsi6gklBgtDzuWIJ5LaPxvMDkKW49p4cWAygVE9CdQp_Cz5jx0ON1EeVM34oZECvbM1NB5g5G4NVxZkcz4SLar45Q==',
        "MarketingSpecialist2": b'gAAAAABpPSsiPd_zYG4OqBOI0RFT-l-qYOhFXSyAdhSXNKOFrW8VhGMmqs4ZYTcKFffI_q-UBNY3lQxpoufsI7bjVHUwhzq7PKWHUboR8hoSOskihd8mWis=',
        "SocialMediaManager": b'gAAAAABpPSsiP4TocwvkhR5xJHy2Y79Q7aUs_j9zRPb0yk27DpxaxpaAMp1_b5tCvGlxESGslgzDSdcDFkfKPywzEEQU8wlvNWJlOMYAoc9XZGJsd0UUI28=',
        "ContentCreator1": b'gAAAAABpPSsiE7uTV2lSL76HhVAGibbJpMFwTXHZSDRSjAL_CnMXUJXiTZcAsTbB4utgl2A53mn4RPNKyzIeqLPynq8Qo6F957jjulSyjlHChXz0lR-256Q=',
        "ContentCreator2": b'gAAAAABpPSsiD3uBzFF9xCoB-0FSp3yZGGhgm1FNS6COIXsnb4vqwg0mK6rI_30LoYhRtSbb69ltNhflwUEmhGj_5YYiswlDEL2hJ6hKzFGMLYjEwTeKtoQ3CiEAwJyMhETlB4q05qKc6gwg1z1_OJekz3qQW47zUA==',

        # Sales branch
        "SalesHead": b'gAAAAABpPSsiD_HcWWA5VujePb00KhUT4kUZ_setIN0haXpYRByDCqr8Sn1bvXVdnUPkasZShgsQXlf7BK5O6w2dCS1xX44oLQmDZlK2O4mo-6M13vi9M30=',
        "SalesManager1": b'gAAAAABpPSsi0WC70zeRdyGtKisE8ZwsUtzn15w7Xlad3BT4PS5TYIqMp98LeOlkJ7grMb9xb17oxYY6oAMcXhp9xjZEd9ltRIpRWd2AHMJGw3mw5dBoYxA2gdTw5UJjdZuVP9b_AJ9M',
        "SalesManager2": b'gAAAAABpPSsiT7YWVc1V06czJgfIsM0aguUI4ThFQex0naHl7U0HkP6V-fkKr5uEQCsxzXG2uKTtFf_taEHtaYbTtVWrmMqwWb_F41sf0rEoQ3UHsTR6jQI=',
        "SalesRep1": b'gAAAAABpPSsiGKw96U9jzLM2KAoqAjSchqU_HtYx9jJaY0cM09gPHEnQFpSP1JFJmqv9AYOM-CmIXa38CZPjpjKibqCNO8z4iw==',
        "SalesRep2": b'gAAAAABpPSsioUCoFEkPFtkcCNz-_I1FerxwVCXv1aJbFmF1bRO5xPFvQv-dyUIrGH_hK315RTa_S1T8wmp8KSA7rFToqt4mrg==',
        "SalesRep3": b'gAAAAABpPSsignk586fUhO_GebOUKFCD54dDrXMZsBfjt3B1HSE_LTbhDWmw3NUX5g5QfCumQDA70QVxVnt90vya3FTi2wCDjg==',

        # Finance branch
        "FinanceHead": b'gAAAAABpPSsiZcUrzKF5oouiv6r6-Kj59AhwBpU8XSl2mU90qemlfNQSSyHLs4Nlt4dJNsn_OI-mbs-IvU6lGffvpb2k9H9Y04fHbFjqoJG9NQu8wR_Rlo0=',
        "Accountant1": b'gAAAAABpPSsinYFLvlfI3qaIdY5nFCWqQ9ahhN0cXGiPC5pcxVLx2iMmAWwmaSkiW2ULiDyb9WB2kRth1d-gFiFfEZMFQWIrkgplfMax9xA2xADzuGBlOGI=',
        "Accountant2": b'gAAAAABpPSsiV1HdD56ytdC8O830ADFcl3uRgCUTyqZK0ZNi_3XjbWmvq3PQX2oAMrnL73iuNtmHQy5fXj8Y35IrwTQiFKsWF7Rd7-CjAJxYOzr0NoOjIAY=',

        # Operations branch
        "OperationsHead": b'gAAAAABpPSsiBzXgls2VLepQMiXZzoh9o-QPTUQHF-99_2UG-ZwHy9lfkJ9G1y9fsDusLl0icMalU-Bi2UhMDjjP5grD3J6piUYFn67h1bGXoYlyei6IoNlQmnKY25AwL6bLTTI2OeBA',
    }


    infoNodes = {}

    for key, data in messagesData.items():
        infoNodes[key] = infoBranchNode(data, key)

    return infoNodes