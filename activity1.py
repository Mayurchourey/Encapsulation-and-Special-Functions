class myClass:
      __privatevar = 27

      def __privaMeth(self):
            print("I'm inside class myClass")

      def hello(self):
            print("Private variable value:", myClass.__privatevar)

# Object creator and method call
too = myClass()
too.hello()
