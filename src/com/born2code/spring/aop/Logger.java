package com.born2code.spring.aop;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class Logger {


    /* Sample PCD PointCut Designation: within, this, execute, target */

    /* reusablePointCut */
    @Pointcut("within(@org.springframework.stereotype.Component com.born2code.spring..*)")
    public void somePointcut() {
    }

    @Before("somePointcut()")
    public void somePointcutDemo() {
        System.out.println("*********** Before DEMO *********");
    }
}
