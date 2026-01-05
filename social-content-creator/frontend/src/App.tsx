import { useState } from 'react';
import { Sparkles, MessageSquare, User, Menu, X } from 'lucide-react';
import { ChatInterface } from './components/ChatInterface';
import { ProfileAnalyzer } from './components/ProfileAnalyzer';
import { ContentCreator } from './components/ContentCreator';

type Tab = 'create' | 'chat' | 'analyze';

function App() {
  const [activeTab, setActiveTab] = useState<Tab>('create');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const tabs = [
    { id: 'create' as Tab, label: 'Criar Conteudo', icon: Sparkles },
    { id: 'chat' as Tab, label: 'Chat', icon: MessageSquare },
    { id: 'analyze' as Tab, label: 'Analisar Perfil', icon: User },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-3">
              <div className="p-2 bg-gradient-to-br from-primary-400 to-primary-600 rounded-xl">
                <Sparkles className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-900">Social Content Creator</h1>
                <p className="text-xs text-gray-500 hidden sm:block">Powered by Agno AI Agents</p>
              </div>
            </div>

            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="sm:hidden p-2 text-gray-500 hover:text-gray-700"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>

            <nav className="hidden sm:flex items-center gap-1">
              {tabs.map((tab) => {
                const Icon = tab.icon;
                return (
                  <button
                    key={tab.id}
                    onClick={() => setActiveTab(tab.id)}
                    className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition-colors ${
                      activeTab === tab.id
                        ? 'bg-primary-50 text-primary-600'
                        : 'text-gray-600 hover:bg-gray-100'
                    }`}
                  >
                    <Icon className="w-4 h-4" />
                    {tab.label}
                  </button>
                );
              })}
            </nav>
          </div>

          {mobileMenuOpen && (
            <nav className="sm:hidden py-4 border-t border-gray-200">
              {tabs.map((tab) => {
                const Icon = tab.icon;
                return (
                  <button
                    key={tab.id}
                    onClick={() => {
                      setActiveTab(tab.id);
                      setMobileMenuOpen(false);
                    }}
                    className={`flex items-center gap-2 w-full px-4 py-3 rounded-lg font-medium transition-colors ${
                      activeTab === tab.id
                        ? 'bg-primary-50 text-primary-600'
                        : 'text-gray-600 hover:bg-gray-100'
                    }`}
                  >
                    <Icon className="w-4 h-4" />
                    {tab.label}
                  </button>
                );
              })}
            </nav>
          )}
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h2 className="text-2xl font-bold text-gray-800">
            {activeTab === 'create' && 'Criar Conteudo com IA'}
            {activeTab === 'chat' && 'Chat com Content Master'}
            {activeTab === 'analyze' && 'Analisar Perfil de Referencia'}
          </h2>
          <p className="text-gray-500 mt-1">
            {activeTab === 'create' && 'Preencha os campos e deixe a IA criar seu conteudo pronto para postar'}
            {activeTab === 'chat' && 'Converse livremente com o agente para criar qualquer tipo de conteudo'}
            {activeTab === 'analyze' && 'Analise perfis de sucesso para aprender com eles'}
          </p>
        </div>

        {activeTab === 'create' && <ContentCreator />}
        {activeTab === 'chat' && <ChatInterface />}
        {activeTab === 'analyze' && <ProfileAnalyzer />}
      </main>

      <footer className="bg-white border-t border-gray-200 mt-auto">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <p className="text-center text-sm text-gray-500">
            Social Content Creator - Sistema Multiagente com Agno Framework
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;
