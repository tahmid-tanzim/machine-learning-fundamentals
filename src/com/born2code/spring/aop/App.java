package com.born2code.spring.aop;

import com.born2code.spring.camera.accessories.Lens;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("com/born2code/spring/aop/beans.xml");
        ICamera camera = (ICamera) context.getBean("camera");
        Lens lens = (Lens) context.getBean("lens");

        camera.snap();
        camera.snap(500);
        camera.snap(1.8);
        camera.snap(500, 1.8);
        camera.snapNightTime();

        lens.zoom(5);

        Car car = (Car) context.getBean("car");
        camera.snapCar(car);
        ((ClassPathXmlApplicationContext) context).close();
    }
}

