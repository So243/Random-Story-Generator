import random
import tkinter as tk

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

def generate_story():
    story = (
        random.choice(when) + ', ' +
        random.choice(who) + ' that lived in ' +
        random.choice(residence) + ', went to the ' +
        random.choice(went) + ' and ' +
        random.choice(happened)
    )
    story_var.set(story)

root = tk.Tk()
root.title("Random Story Generator")

story_var = tk.StringVar()
story_label = tk.Label(root, textvariable=story_var, wraplength=400, padx=10, pady=10)
story_label.pack(pady=10)

generate_btn = tk.Button(root, text="Generate Story", command=generate_story)
generate_btn.pack(pady=5)

root.mainloop()
