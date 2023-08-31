import sound_input.sound_input as si
import cmd_ps.pgm_start as ps
import txt_ps.text_ps as tp

sound = si.Sound_listen()
cmd = ps.Start_pgm("./cmd_ps/pgm_dict.txt")
text_ps = tp.Text_ps()

text = sound.listen()

if text != False and text != "":
    text_ps.text_ps()