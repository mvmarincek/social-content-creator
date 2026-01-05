import { useState, useRef } from 'react';
import { Sparkles, Loader2, Copy, Check, Upload, X, Image, Music, Video } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import { createContent } from '../lib/api';
import type { Platform, ContentType, ToneOfVoice } from '../lib/types';

const platforms: { value: Platform; label: string }[] = [
  { value: 'instagram', label: 'Instagram' },
  { value: 'tiktok', label: 'TikTok' },
  { value: 'youtube', label: 'YouTube' },
  { value: 'linkedin', label: 'LinkedIn' },
  { value: 'twitter', label: 'X (Twitter)' },
];

const contentTypes: { value: ContentType; label: string }[] = [
  { value: 'post', label: 'Post' },
  { value: 'reels', label: 'Reels' },
  { value: 'stories', label: 'Stories' },
  { value: 'carousel', label: 'Carrossel' },
  { value: 'video', label: 'Video' },
  { value: 'short', label: 'Short' },
];

const tones: { value: ToneOfVoice; label: string }[] = [
  { value: 'casual', label: 'Casual' },
  { value: 'professional', label: 'Profissional' },
  { value: 'motivational', label: 'Motivacional' },
  { value: 'educational', label: 'Educativo' },
  { value: 'humorous', label: 'Humoristico' },
  { value: 'inspirational', label: 'Inspiracional' },
];

interface UploadedFile {
  file: File;
  preview: string;
  type: 'image' | 'audio' | 'video';
}

export function ContentCreator() {
  const [description, setDescription] = useState('');
  const [platform, setPlatform] = useState<Platform>('instagram');
  const [contentType, setContentType] = useState<ContentType>('post');
  const [tone, setTone] = useState<ToneOfVoice>('casual');
  const [referenceProfile, setReferenceProfile] = useState('');
  const [referenceText, setReferenceText] = useState('');
  const [userCopy, setUserCopy] = useState('');
  const [generateImage, setGenerateImage] = useState(false);
  const [generateVideo, setGenerateVideo] = useState(false);
  const [generateAudio, setGenerateAudio] = useState(false);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);
  const [uploadedFiles, setUploadedFiles] = useState<UploadedFile[]>([]);

  const imageInputRef = useRef<HTMLInputElement>(null);
  const audioInputRef = useRef<HTMLInputElement>(null);
  const videoInputRef = useRef<HTMLInputElement>(null);

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>, type: 'image' | 'audio' | 'video') => {
    const files = e.target.files;
    if (!files) return;

    Array.from(files).forEach((file) => {
      const preview = type === 'image' ? URL.createObjectURL(file) : '';
      setUploadedFiles((prev) => [...prev, { file, preview, type }]);
    });

    e.target.value = '';
  };

  const removeFile = (index: number) => {
    setUploadedFiles((prev) => {
      const newFiles = [...prev];
      if (newFiles[index].preview) {
        URL.revokeObjectURL(newFiles[index].preview);
      }
      newFiles.splice(index, 1);
      return newFiles;
    });
  };

  const handleCreate = async () => {
    if (!description.trim()) return;

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const filesDescription = uploadedFiles.length > 0
        ? `\n\nArquivos anexados pelo usuario:\n${uploadedFiles.map((f, i) => `${i + 1}. ${f.type}: ${f.file.name}`).join('\n')}`
        : '';

      const response = await createContent({
        description: description + filesDescription,
        platform,
        content_type: contentType,
        tone,
        reference_profile: referenceProfile || undefined,
        reference_text: referenceText || undefined,
        user_copy: userCopy || undefined,
        generate_image: generateImage,
        generate_video: generateVideo,
        generate_audio: generateAudio,
      });

      if (response.success) {
        setResult(response.content);
      } else {
        setError(response.error || 'Erro ao criar conteudo');
      }
    } catch (err) {
      setError('Erro ao conectar com o servidor. Verifique se o backend esta rodando.');
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = () => {
    if (result) {
      navigator.clipboard.writeText(result);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const imageFiles = uploadedFiles.filter((f) => f.type === 'image');
  const audioFiles = uploadedFiles.filter((f) => f.type === 'audio');
  const videoFiles = uploadedFiles.filter((f) => f.type === 'video');

  return (
    <div className="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
      <div className="flex items-center gap-3 mb-6">
        <div className="p-2 bg-gradient-to-br from-primary-400 to-primary-600 rounded-lg">
          <Sparkles className="w-6 h-6 text-white" />
        </div>
        <div>
          <h2 className="text-xl font-bold text-gray-800">Criar Conteudo</h2>
          <p className="text-sm text-gray-500">Descreva o que voce precisa e deixe a IA criar</p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Plataforma</label>
          <select
            value={platform}
            onChange={(e) => setPlatform(e.target.value as Platform)}
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
          >
            {platforms.map((p) => (
              <option key={p.value} value={p.value}>{p.label}</option>
            ))}
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Tipo</label>
          <select
            value={contentType}
            onChange={(e) => setContentType(e.target.value as ContentType)}
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
          >
            {contentTypes.map((t) => (
              <option key={t.value} value={t.value}>{t.label}</option>
            ))}
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Tom</label>
          <select
            value={tone}
            onChange={(e) => setTone(e.target.value as ToneOfVoice)}
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
          >
            {tones.map((t) => (
              <option key={t.value} value={t.value}>{t.label}</option>
            ))}
          </select>
        </div>
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-2">Descreva seu conteudo *</label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Ex: Quero criar um Reels sobre 5 dicas de produtividade para empreendedores iniciantes, com tom motivacional e moderno..."
          rows={4}
          className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 resize-none"
        />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-3">Anexar Arquivos (opcional)</label>
        <div className="flex flex-wrap gap-3">
          <input
            ref={imageInputRef}
            type="file"
            accept="image/*"
            multiple
            onChange={(e) => handleFileUpload(e, 'image')}
            className="hidden"
          />
          <input
            ref={audioInputRef}
            type="file"
            accept="audio/*"
            multiple
            onChange={(e) => handleFileUpload(e, 'audio')}
            className="hidden"
          />
          <input
            ref={videoInputRef}
            type="file"
            accept="video/*"
            multiple
            onChange={(e) => handleFileUpload(e, 'video')}
            className="hidden"
          />

          <button
            type="button"
            onClick={() => imageInputRef.current?.click()}
            className="flex items-center gap-2 px-4 py-2 border-2 border-dashed border-gray-300 rounded-lg hover:border-primary-400 hover:bg-primary-50 transition-colors"
          >
            <Image className="w-5 h-5 text-gray-500" />
            <span className="text-sm text-gray-600">Fotos</span>
          </button>

          <button
            type="button"
            onClick={() => audioInputRef.current?.click()}
            className="flex items-center gap-2 px-4 py-2 border-2 border-dashed border-gray-300 rounded-lg hover:border-primary-400 hover:bg-primary-50 transition-colors"
          >
            <Music className="w-5 h-5 text-gray-500" />
            <span className="text-sm text-gray-600">Audio</span>
          </button>

          <button
            type="button"
            onClick={() => videoInputRef.current?.click()}
            className="flex items-center gap-2 px-4 py-2 border-2 border-dashed border-gray-300 rounded-lg hover:border-primary-400 hover:bg-primary-50 transition-colors"
          >
            <Video className="w-5 h-5 text-gray-500" />
            <span className="text-sm text-gray-600">Video</span>
          </button>
        </div>

        {uploadedFiles.length > 0 && (
          <div className="mt-4 space-y-3">
            {imageFiles.length > 0 && (
              <div>
                <p className="text-xs text-gray-500 mb-2">Imagens ({imageFiles.length})</p>
                <div className="flex flex-wrap gap-2">
                  {imageFiles.map((f, i) => (
                    <div key={i} className="relative group">
                      <img
                        src={f.preview}
                        alt={f.file.name}
                        className="w-20 h-20 object-cover rounded-lg border border-gray-200"
                      />
                      <button
                        onClick={() => removeFile(uploadedFiles.indexOf(f))}
                        className="absolute -top-2 -right-2 p-1 bg-red-500 text-white rounded-full opacity-0 group-hover:opacity-100 transition-opacity"
                      >
                        <X className="w-3 h-3" />
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {audioFiles.length > 0 && (
              <div>
                <p className="text-xs text-gray-500 mb-2">Audios ({audioFiles.length})</p>
                <div className="flex flex-wrap gap-2">
                  {audioFiles.map((f, i) => (
                    <div key={i} className="flex items-center gap-2 px-3 py-2 bg-gray-100 rounded-lg">
                      <Music className="w-4 h-4 text-gray-500" />
                      <span className="text-sm text-gray-700 max-w-[150px] truncate">{f.file.name}</span>
                      <button
                        onClick={() => removeFile(uploadedFiles.indexOf(f))}
                        className="p-1 hover:bg-gray-200 rounded-full"
                      >
                        <X className="w-3 h-3 text-gray-500" />
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {videoFiles.length > 0 && (
              <div>
                <p className="text-xs text-gray-500 mb-2">Videos ({videoFiles.length})</p>
                <div className="flex flex-wrap gap-2">
                  {videoFiles.map((f, i) => (
                    <div key={i} className="flex items-center gap-2 px-3 py-2 bg-gray-100 rounded-lg">
                      <Video className="w-4 h-4 text-gray-500" />
                      <span className="text-sm text-gray-700 max-w-[150px] truncate">{f.file.name}</span>
                      <button
                        onClick={() => removeFile(uploadedFiles.indexOf(f))}
                        className="p-1 hover:bg-gray-200 rounded-full"
                      >
                        <X className="w-3 h-3 text-gray-500" />
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Perfil de Referencia (opcional)</label>
          <input
            type="text"
            value={referenceProfile}
            onChange={(e) => setReferenceProfile(e.target.value)}
            placeholder="https://instagram.com/exemplo"
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Sua Copy/Texto (opcional)</label>
          <input
            type="text"
            value={userCopy}
            onChange={(e) => setUserCopy(e.target.value)}
            placeholder="Texto que voce ja tem preparado..."
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        </div>
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-2">Texto de Referencia para Estilo (opcional)</label>
        <textarea
          value={referenceText}
          onChange={(e) => setReferenceText(e.target.value)}
          placeholder="Cole aqui um texto de referencia para o sistema aprender o estilo..."
          rows={3}
          className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 resize-none"
        />
      </div>

      <div className="mb-6">
        <label className="block text-sm font-medium text-gray-700 mb-3">Gerar com IA</label>
        <div className="flex flex-wrap gap-4">
          <label className="flex items-center gap-2 cursor-pointer">
            <input
              type="checkbox"
              checked={generateImage}
              onChange={(e) => setGenerateImage(e.target.checked)}
              className="w-4 h-4 text-primary-500 rounded focus:ring-primary-500"
            />
            <span className="text-sm text-gray-700">Imagem</span>
          </label>
          <label className="flex items-center gap-2 cursor-pointer">
            <input
              type="checkbox"
              checked={generateVideo}
              onChange={(e) => setGenerateVideo(e.target.checked)}
              className="w-4 h-4 text-primary-500 rounded focus:ring-primary-500"
            />
            <span className="text-sm text-gray-700">Video</span>
          </label>
          <label className="flex items-center gap-2 cursor-pointer">
            <input
              type="checkbox"
              checked={generateAudio}
              onChange={(e) => setGenerateAudio(e.target.checked)}
              className="w-4 h-4 text-primary-500 rounded focus:ring-primary-500"
            />
            <span className="text-sm text-gray-700">Narracao</span>
          </label>
        </div>
      </div>

      <button
        onClick={handleCreate}
        disabled={loading || !description.trim()}
        className="w-full px-6 py-4 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-lg hover:from-primary-600 hover:to-primary-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all font-semibold flex items-center justify-center gap-2"
      >
        {loading ? (
          <>
            <Loader2 className="w-5 h-5 animate-spin" />
            Criando conteudo...
          </>
        ) : (
          <>
            <Sparkles className="w-5 h-5" />
            Criar Conteudo
          </>
        )}
      </button>

      {error && (
        <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700">
          {error}
        </div>
      )}

      {result && (
        <div className="mt-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
          <div className="flex items-center justify-between mb-3">
            <h3 className="font-semibold text-gray-800">Conteudo Gerado</h3>
            <button
              onClick={handleCopy}
              className="flex items-center gap-1 px-3 py-1 text-sm bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
            >
              {copied ? (
                <>
                  <Check className="w-4 h-4 text-green-500" />
                  Copiado!
                </>
              ) : (
                <>
                  <Copy className="w-4 h-4" />
                  Copiar
                </>
              )}
            </button>
          </div>
          <div className="markdown-content text-gray-700">
            <ReactMarkdown>{result}</ReactMarkdown>
          </div>
        </div>
      )}
    </div>
  );
}
