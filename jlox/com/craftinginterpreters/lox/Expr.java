package com.craftinginterpreters.lox

import java.util.List;

abstract classExpr {
  interface Visitor<R>  {
   R visitBinaryExpr(Binary expr);
   R visitGroupingExpr(Grouping expr);
   R visitLiteralExpr(Literal expr);
   R visitUnaryExpr(Unary expr);
  }
 static class Binary extends Expr {
      this.left = left;
      this.operator = operator;
      this.right = right;
   }

   @Override
   <R> R accept(Visitor<R> Visitor) {
    return visitor.visitBinaryExpr(this);
   }

   final Expr left;
   final Token operator;
   final Expr right;
  }
 static class Grouping extends Expr {
      this.expression = expression;
   }

   @Override
   <R> R accept(Visitor<R> Visitor) {
    return visitor.visitGroupingExpr(this);
   }

   final Expr expression;
  }
 static class Literal extends Expr {
      this.value = value;
   }

   @Override
   <R> R accept(Visitor<R> Visitor) {
    return visitor.visitLiteralExpr(this);
   }

   final Object value;
  }
 static class Unary extends Expr {
      this.operator = operator;
      this.right = right;
   }

   @Override
   <R> R accept(Visitor<R> Visitor) {
    return visitor.visitUnaryExpr(this);
   }

   final Token operator;
   final Expr right;
  }
}
  abstract <R> R accept(Visitor<R> visitor);
