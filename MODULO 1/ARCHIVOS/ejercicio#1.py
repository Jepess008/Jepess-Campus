import io
text =open("MODULO 1/ARCHIVOS/Enviados.txt", "w", encoding="utf-8")
fd = open("MODULO 1/ARCHIVOS/mbox-short.txt", "r", encoding="utf-8")
emails= []
for x in fd:
    if x.startswith("From: "):
        x= x[6:]
        emails.append(x)

sent= set(emails)
sent= list(sent)
for i in range(len(sent)-1, 0, -1):
    x=sent[i]
    print("Enviado OK\t", x.rstrip())
text.writelines(sent)
fd.close()

