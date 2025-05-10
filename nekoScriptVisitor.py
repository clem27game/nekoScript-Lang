# Generated from nekoScript.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .nekoScriptParser import nekoScriptParser
else:
    from nekoScriptParser import nekoScriptParser

# This class defines a complete generic visitor for a parse tree produced by nekoScriptParser.

class nekoScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by nekoScriptParser#script.
    def visitScript(self, ctx:nekoScriptParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#instruction.
    def visitInstruction(self, ctx:nekoScriptParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#affectation.
    def visitAffectation(self, ctx:nekoScriptParser.AffectationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#operation.
    def visitOperation(self, ctx:nekoScriptParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#appelFonction.
    def visitAppelFonction(self, ctx:nekoScriptParser.AppelFonctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#importation.
    def visitImportation(self, ctx:nekoScriptParser.ImportationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#blocSite.
    def visitBlocSite(self, ctx:nekoScriptParser.BlocSiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#contenuSite.
    def visitContenuSite(self, ctx:nekoScriptParser.ContenuSiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#styleInstruction.
    def visitStyleInstruction(self, ctx:nekoScriptParser.StyleInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#packageDeclaration.
    def visitPackageDeclaration(self, ctx:nekoScriptParser.PackageDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#packageInstruction.
    def visitPackageInstruction(self, ctx:nekoScriptParser.PackageInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#paramList.
    def visitParamList(self, ctx:nekoScriptParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#terminalCommand.
    def visitTerminalCommand(self, ctx:nekoScriptParser.TerminalCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#appelExterne.
    def visitAppelExterne(self, ctx:nekoScriptParser.AppelExterneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#valeur.
    def visitValeur(self, ctx:nekoScriptParser.ValeurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#operateur.
    def visitOperateur(self, ctx:nekoScriptParser.OperateurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nekoScriptParser#commentaire.
    def visitCommentaire(self, ctx:nekoScriptParser.CommentaireContext):
        return self.visitChildren(ctx)



del nekoScriptParser