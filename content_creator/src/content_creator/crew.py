from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool

agents_config = 'config/agents.yaml'
tasks_config = 'config/tasks.yaml'


@CrewBase
class ContentCreator():
    """ContentCreator crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def product_competitor_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['product_competitor_researcher'],  
            verbose=True,
            tools = [SerperDevTool()]
        )

    @agent
    def strategy_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['strategy_planner'],  
            verbose=True
        )

    @agent
    def creative_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_content_creator'],  
            verbose=True
        )

    @agent
    def senior_photographer(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_photographer'],  
            verbose=True
        )

    @agent
    def chief_creative_director(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_creative_director'],  
            verbose=True
        )

    @agent
    def adapter(self) -> Agent:
        return Agent(
            config=self.agents_config['adapter'],  
            verbose=True
        )

    @agent
    def ab_variant_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['ab_variant_generator'],  
            verbose=True
        )

    @task
    def website_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['website_analysis'],  
        )

    @task
    def market_anaysis(self) -> Task:
        return Task(
            config=self.tasks_config['market_anaysis'],  
        )

    @task
    def campaign_develpoment(self) -> Task:
        return Task(
            config=self.tasks_config['campaign_develpoment'],  
        )

    @task
    def ab_variant_task(self) -> Task:
        return Task(
            config=self.tasks_config['ab_variant_task'],  
        )

    @task
    def write_copy(self) -> Task:
        return Task(
            config=self.tasks_config['write_copy'],  
        )

    @task
    def take_photo(self) -> Task:
        return Task(
            config=self.tasks_config['take_photo'],  
        )

    @task
    def approval_photo(self) -> Task:
        return Task(
            config=self.tasks_config['approval_photo'],  
        )

    @task
    def adapter_task(self) -> Task:
        return Task(
            config=self.tasks_config['adapter_task'],  
            output_file="output/final_platform_content.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ContentCreator Crew """

        manager = Agent(
            config =self.agents_config['manager'],
            allow_delegation = True
            verbose=True
        )

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical
            manager_agent= manager
            verbose=True    
        )