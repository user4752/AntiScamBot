from CommandHelpers import TargetIdTransformer
from discord import app_commands, Interaction, Member, Embed
from ScamReportModal import SubmitScamReport
from Config import Config

@app_commands.guild_only()
class GlobalScamCommands(app_commands.Group):   
    def GetInstance(self):
        return self.extras["instance"]
     
    @app_commands.command(name="check", description="Checks to see if a discord id is banned")
    @app_commands.checks.has_permissions(ban_members=True)
    @app_commands.checks.cooldown(1, 5.0)
    async def ScamCheck_Global(self, interaction:Interaction, target:app_commands.Transform[int, TargetIdTransformer]):
        if (target <= -1):
            await interaction.response.send_message("Invalid id!", ephemeral=True, delete_after=5.0)
            return
        
        if (self.GetInstance().Database.IsActivatedInServer(interaction.guild_id)):
            ResponseEmbed:Embed = await self.GetInstance().CreateBanEmbed(target)
            await interaction.response.send_message(embed = ResponseEmbed)
        else:
            await interaction.response.send_message("You must be activated in order to run scam check!")

    @app_commands.command(name="report", description="Report an User ID")
    @app_commands.checks.has_permissions(ban_members=True)
    @app_commands.checks.cooldown(1, 5.0)
    async def ReportScam_Global(self, interaction:Interaction, target:app_commands.Transform[int, TargetIdTransformer]):        
        if (interaction.guild_id == Config()["ControlServer"]):
            await interaction.response.send_message("You cannot make remote reports from this server!", ephemeral=True, delete_after=5.0)
            return
        
        UserToSend:Member = await self.GetInstance().LookupUser(target, ServerToInspect=interaction.guild)
        await interaction.response.send_modal(SubmitScamReport(UserToSend))
        
    @app_commands.command(name="reportuser", description="Report a mentionable member")
    @app_commands.checks.has_permissions(ban_members=True)
    @app_commands.checks.cooldown(1, 5.0)
    async def ReportScamUser_Global(self, interaction:Interaction, user:Member):
        if (interaction.guild_id == Config()["ControlServer"]):
            await interaction.response.send_message("You cannot make remote reports from this server!", ephemeral=True, delete_after=5.0)
            return
        
        await interaction.response.send_modal(SubmitScamReport(user))