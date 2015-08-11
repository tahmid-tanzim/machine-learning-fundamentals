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
        lens.zoom(5);

        ((ClassPathXmlApplicationContext) context).close();
    }
}

