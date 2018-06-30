apetece_un_helado_input = input("Quieres un helado? (Si/No) ").upper()

if apetece_un_helado_input == "SI":
    apetece_un_helado = True
elif apetece_un_helado_input == "NO":
    apetece_un_helado = False
else:
    print("Te he dicho que me digas Si o NO y me has respondido otra cosa asi que te lo cuento como no")
    apetece_un_helado=false


tienes_dinero_input = input("Tienes dinero? (Si/No)" ).upper()

if tienes_dinero_input == "SI":
    tienes_dinero = True
elif tienes_dinero_input == "NO":
    tienes_dinero = False
else:
    print("Te he dicho que me digas Si o NO y me has respondido otra cosa asi que te lo cuento como no")
    tienes_dinero=false


estas_con_tu_tia = input("Estas con tu tia? (Si/No" ).upper()

if estas_con_tu_tia == "SI":
    tu_tia = True
elif estas_con_tu_tia == "NO":
    tu_tia = False
else:
    print("Te he dicho que me digas Si o NO y me has respondido otra cosa asi que te lo cuento como no")
    apetece_un_helado=false

puedes_comprarlo = tu_tia or tienes_dinero


if apetece_un_helado and puedes_comprarlo:
    print("Compra uno")

else:
    print("No te lo compres")