package com.born2code.spring.aop;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("com/born2code/spring/aop/beans.xml");

        IBlender blender = (IBlender) context.getBean("blender");
        ((IMachine)blender).start();
        blender.blend();

        IFan fan = (IFan) context.getBean("fan");
        ((IMachine)fan).start();
        fan.activate(5);

        ((ClassPathXmlApplicationContext) context).close();
    }
}

