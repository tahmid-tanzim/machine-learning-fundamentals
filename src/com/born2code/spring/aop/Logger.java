package com.born2code.spring.aop;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class Logger {


    /* Sample PCD PointCut Designation: within, this, execute, target */

    /* reusablePointCut */
    @Pointcut("target(com.born2code.spring.aop.Camera)")
    public void somePointcut() {
    }

    @Before("somePointcut()")
    public void somePointcutDemo(JoinPoint joinPoint) {
        System.out.println("*********** Before DEMO *********");
        for(Object object : joinPoint.getArgs()) {
            System.out.println("Arg: " + object);
        }
    }


}
