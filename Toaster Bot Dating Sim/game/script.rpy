# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define e = Character('', color="#c8ffc8")
image toaster_horny = Image("/images/donkey.png", xpos=0, ypos=0)

# Hier beginnt das Spiel.
label start:

    e "Toaster Bot is coming for you..."

    e "be prepared"
    scene kitchen
    play audio "okay.mp3"
    show toaster_horny with dissolve:
      xpos 1000
      ypos 600
      linear 3.0 xpos 1000 ypos 600

    "hey"

    return
