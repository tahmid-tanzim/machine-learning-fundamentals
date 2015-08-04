package com.born2code.spring.aop;

import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class Logger {

    /* reusablePointCut */
    @Pointcut("execution(* com.born2code.spring.aop.Camera.*(..))")
    public void cameraSnap(){}

    /* reusablePointCut */
    @Pointcut("execution(* *.*(..))")
    public void cameraActivity(){}

    @Before("cameraSnap()")
    public void aboutToTakePhoto() {
        System.out.println("About To Take Photo...");
    }

    @After("cameraSnap()")
    public void theEnd() {
        System.out.println("Bye...");
    }

    @Before("cameraActivity()")
    public void cameraRelatedActivity() {
        System.out.println("Doing something related to cameras...");
    }
}
