import fire

def hello(name="World"):
  return "Hello Naw %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
