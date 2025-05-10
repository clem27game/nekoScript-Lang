# Generated from nekoScript.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .nekoScriptParser import nekoScriptParser
else:
    from nekoScriptParser import nekoScriptParser

# This class defines a complete listener for a parse tree produced by nekoScriptParser.
class nekoScriptListener(ParseTreeListener):

    # Enter a parse tree produced by nekoScriptParser#script.
    def enterScript(self, ctx:nekoScriptParser.ScriptContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#script.
    def exitScript(self, ctx:nekoScriptParser.ScriptContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#instruction.
    def enterInstruction(self, ctx:nekoScriptParser.InstructionContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#instruction.
    def exitInstruction(self, ctx:nekoScriptParser.InstructionContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#affectation.
    def enterAffectation(self, ctx:nekoScriptParser.AffectationContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#affectation.
    def exitAffectation(self, ctx:nekoScriptParser.AffectationContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#operation.
    def enterOperation(self, ctx:nekoScriptParser.OperationContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#operation.
    def exitOperation(self, ctx:nekoScriptParser.OperationContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#appelFonction.
    def enterAppelFonction(self, ctx:nekoScriptParser.AppelFonctionContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#appelFonction.
    def exitAppelFonction(self, ctx:nekoScriptParser.AppelFonctionContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#importation.
    def enterImportation(self, ctx:nekoScriptParser.ImportationContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#importation.
    def exitImportation(self, ctx:nekoScriptParser.ImportationContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#blocSite.
    def enterBlocSite(self, ctx:nekoScriptParser.BlocSiteContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#blocSite.
    def exitBlocSite(self, ctx:nekoScriptParser.BlocSiteContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#contenuSite.
    def enterContenuSite(self, ctx:nekoScriptParser.ContenuSiteContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#contenuSite.
    def exitContenuSite(self, ctx:nekoScriptParser.ContenuSiteContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#styleInstruction.
    def enterStyleInstruction(self, ctx:nekoScriptParser.StyleInstructionContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#styleInstruction.
    def exitStyleInstruction(self, ctx:nekoScriptParser.StyleInstructionContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:nekoScriptParser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:nekoScriptParser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#packageInstruction.
    def enterPackageInstruction(self, ctx:nekoScriptParser.PackageInstructionContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#packageInstruction.
    def exitPackageInstruction(self, ctx:nekoScriptParser.PackageInstructionContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#paramList.
    def enterParamList(self, ctx:nekoScriptParser.ParamListContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#paramList.
    def exitParamList(self, ctx:nekoScriptParser.ParamListContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#terminalCommand.
    def enterTerminalCommand(self, ctx:nekoScriptParser.TerminalCommandContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#terminalCommand.
    def exitTerminalCommand(self, ctx:nekoScriptParser.TerminalCommandContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#appelExterne.
    def enterAppelExterne(self, ctx:nekoScriptParser.AppelExterneContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#appelExterne.
    def exitAppelExterne(self, ctx:nekoScriptParser.AppelExterneContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#valeur.
    def enterValeur(self, ctx:nekoScriptParser.ValeurContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#valeur.
    def exitValeur(self, ctx:nekoScriptParser.ValeurContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#operateur.
    def enterOperateur(self, ctx:nekoScriptParser.OperateurContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#operateur.
    def exitOperateur(self, ctx:nekoScriptParser.OperateurContext):
        pass


    # Enter a parse tree produced by nekoScriptParser#commentaire.
    def enterCommentaire(self, ctx:nekoScriptParser.CommentaireContext):
        pass

    # Exit a parse tree produced by nekoScriptParser#commentaire.
    def exitCommentaire(self, ctx:nekoScriptParser.CommentaireContext):
        pass



del nekoScriptParser