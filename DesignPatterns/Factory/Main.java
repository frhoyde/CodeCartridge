public class Main {

   public static void main(String[] args) {
      ShapeFactory shapeFactory = new ShapeFactory();

      Shape shape1 = shapeFactory.CreateShape("CIRCLE");

      shape1.draw();

      Shape shape2 = shapeFactory.CreateShape("RECTANGLE");

      shape2.draw();

      Shape shape3 = shapeFactory.CreateShape("SQUARE");

      shape3.draw();
   }
}
