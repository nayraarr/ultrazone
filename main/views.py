from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Mens Tiro Vis Tech Competition Jacket Grey/Lime Green',
        'price': '90',
        'desc' : 'Stay sharp on and off the pitch with the Tiro Vis Tech Competition Jacket. \
            Designed in a sleek grey base with striking lime green accents, this jacket combines sporty style with functional comfort. \
            Lightweight yet durable, it’s built with breathable fabric to keep you cool during training and stylish enough for casual wear. \
            Featuring a full-zip front, stand-up collar, and tailored fit, it’s perfect for athletes and fans who want performance and flair in one piece.'
    }

    return render(request, "main.html", context)
